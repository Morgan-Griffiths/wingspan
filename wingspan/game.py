from enum import Enum, auto
from wingspan.food import Food
from wingspan.helpers import UIState, human_readable_action_dictionary,action_dictionary, GameActions, IntermediateState
from wingspan.player import Player
from wingspan.shared import Shared
from wingspan.birds import WingspanBird
from wingspan.bonus_deck import BonusNames,bonus_name_dictionary_itos
import json
import numpy as np

class GameActions(Enum):
    draw_a_card = auto()
    pick_an_action = auto()
    pick_a_bird_card = auto()
    pick_feeder_food = auto()
    pick_player_food = auto()
    pick_bird_on_board = auto()
    pick_board_location = auto()
    pick_player_to_act = auto()
    initial_discard_cards = auto()
    initial_discard_food = auto()
    discard_bonus_cards = auto()
    calculate_end_of_round_scores = auto()

class GameAction:
    def __init__(self,action,player):
        self.action = action
        self.player = player

class Game:
    def __init__(self, n_players, human_readable=True):
        self.n_players = n_players
        self.human_readable = human_readable
        self.shared = None
        self.players = None
        self.current_player = None
        self.acting_player = None
        self.discarding_cards = False
        self.discarding_food = False
        self.drawing_cards = False
        self.picking_food = False
        self.picking_bird = False
        self.picking_board_location = False
        self.birds = self.load_birds()
        self.action_stack = []

    def load_birds(self):
        with open('birds.json', 'r') as f:
            raw_birds = json.loads(f.read())

        birds = []
        # bonus_names = [x.lower() for x in filter(lambda x: x[0] != '_',dir(BonusNames))]
        for raw_bird in raw_birds:
            birds.append(WingspanBird(**raw_bird))
        return birds
    

    def reset(self):
        self.shared = Shared(self.birds)
        self.players = [Player() for _ in range(self.n_players)]
        self.first_player = 0
        # deal 5 cards to each player
        for p in self.players:
            # add cards
            for _ in range(5):
                p.add_bird_card(self.shared.draw_bird_card())
            # add bonus cards
            for _ in range(2):
                p.add_bonus_card(self.shared.draw_bonus_card())
            # add food
            p.add_food(Food.invertebrate)
            p.add_food(Food.seed)
            p.add_food(Food.fish)
            p.add_food(Food.rodent)
            p.add_food(Food.fruit)

        # add 3 birds to faceup
        for _ in range(3):
            self.shared.faceup.add(self.shared.draw_bird_card())
        # roll dice in feeder
        self.shared.feeder.roll()
        # add 4 end of round goals
        self.shared.goals.draw(4)
        # place start marker
        self.shared.place_start_marker(self.n_players)
        # set current player
        self.acting_player = self.current_player = self.shared.start_marker.position
        # set state
        self.prepopulate_stack()
        # return initial observation
        return self.handle_state()
    
    def handle_state(self):
        current_state = self.action_stack.pop()
        action_vector = self.return_actions(current_state)
        return self.observation(current_state),self.action_vector_to_readable(action_vector), self.done

    def action_vector_to_readable(self,action_vector):
        # use np.where to get indices of nonzero elements
        nonzero_indices = np.where(action_vector > 0)[0]
        if self.players[self.current_player].state == UIState.initial_discard_bonus_cards:
            print(bonus_name_dictionary_itos)
            print(nonzero_indices)
            readable_actions = [bonus_name_dictionary_itos[action_vector[idx]] for idx in nonzero_indices]
        else:
            readable_actions = [action_dictionary[idx] for idx in nonzero_indices]
        return readable_actions
    
    def return_actions(self,situation):
        # construct action vector
        acting_player,action = situation.player,situation.action
        action_vector = np.zeros(len(human_readable_action_dictionary),dtype=int)
        if action == GameActions.initial_discard_cards:
            hand_start = human_readable_action_dictionary['player hand one']
            num_cards = len(self.players[acting_player].hand)
            action_vector[hand_start:hand_start+num_cards] = 1
            action_vector[human_readable_action_dictionary['no op']] = 1
        elif action == GameActions.initial_discard_food:
            current_food = self.players[acting_player].return_food_vector()
            food_start = human_readable_action_dictionary[Food.invertebrate]
            action_vector[food_start:food_start+5] = current_food
        elif action == GameActions.discard_bonus_cards:
            bonus_cards = self.players[acting_player].return_bonus_card_vector()
            bonus_start = human_readable_action_dictionary['player bonus card one']
            action_vector[bonus_start:bonus_start+len(self.players[acting_player].bonus_cards)] = bonus_cards
        elif action == GameActions.pick_an_action:
            # 4 actions
            action_start = human_readable_action_dictionary['play a bird']
            action_vector[action_start:action_start+4] = 1

            if self.players[self.current_player].can_discard_card_to_get_food():
                ...
            if self.shared.feeder.can_reroll():
                ...
        return action_vector
            
    def observation(self,situation:GameAction):
        return f'{situation}\n' + f'{self.players[situation.acting_player].observation()}'
    
    def step(self, action):
        if self.players[self.current_player].state == UIState.initial_discard_cards:
            if action == action_dictionary[GameActions.no_op.get_value()]:
                self.players[self.current_player].state = UIState.initial_discard_food
            else:
                self.players[self.current_player].discard_bird_card(action)
        elif self.players[self.current_player].state == UIState.initial_discard_food:
            self.players[self.current_player].discard_food(action)
            if sum(self.players[self.current_player].return_food_vector()) == 5 - len(self.players[self.current_player].hand):
                self.players[self.current_player].state = UIState.initial_discard_bonus_cards
        elif self.players[self.current_player].state == UIState.initial_discard_bonus_cards:
            self.players[self.current_player].discard_bonus_card(action)
            self.players[self.current_player].state = UIState.round_1
            self.increment_player()
        action_vector = self.return_actions()
        return self.observation(),self.action_vector_to_readable(action_vector), 0, self.done

    
    def prepopulate_stack(self):
        # add card selection
        # add food selection
        # bonus card selection
        for _ in range(self.n_players):
            self.action_stack.append(GameAction(self.acting_player,GameActions.initial_discard_cards))
            self.action_stack.append(GameAction(self.acting_player,GameActions.initial_discard_food))
            self.action_stack.append(GameAction(self.acting_player,GameActions.discard_bonus_cards))
            self.increment_acting_player()
        self.acting_player = self.shared.start_marker.position
        for _ in range(8 * self.n_players):
            self.action_stack.append(GameAction(self.acting_player,GameActions.pick_an_action))
            self.increment_acting_player()
        # calculate round results
        self.action_stack.append(GameAction(_,GameActions.calculate_end_of_round_scores))
        self.shared.increment_start_marker()
        self.acting_player = self.shared.start_marker.position
        for _ in range(7 * self.n_players):
            self.action_stack.append(GameAction(self.acting_player,GameActions.pick_an_action))
            self.increment_acting_player()
        # calculate round results
        self.action_stack.append(GameAction(_,GameActions.calculate_end_of_round_scores))
        self.shared.increment_start_marker()
        self.acting_player = self.shared.start_marker.position
        for _ in range(6 * self.n_players):
            self.action_stack.append(GameAction(self.acting_player,GameActions.pick_an_action))
            self.increment_acting_player()
        # calculate round results
        self.action_stack.append(GameAction(_,GameActions.calculate_end_of_round_scores))
        self.shared.increment_start_marker()
        self.acting_player = self.shared.start_marker.position
        for _ in range(5 * self.n_players):
            self.action_stack.append(GameAction(self.acting_player,GameActions.pick_an_action))
            self.increment_acting_player()
        # calculate round results
        self.action_stack.append(GameAction(_,GameActions.calculate_end_of_round_scores))
        self.action_stack = self.action_stack[::-1]


    def render(self):
        self.shared.render()
        for player in self.players:
            player.render()

    def play(self):
        if self.state == UIState.game_over:
            print("Game over")
            return
        elif self.state == UIState.initial_discard_cards:
            card_names = [
                f"{i} {c.name}"
                for i, c in enumerate(self.players[self.current_player].hand)
            ]
            print(
                f"Current player: {self.current_player} discard cards: {', '.join(card_names)}"
            )
            self.state = UIState.game_over

    @property
    def done(self):
        return self.state == UIState.game_over
    
    def increment_acting_player(self):
        self.acting_player = (self.acting_player + 1) % self.n_players
    
    def increment_player(self):
        self.current_player = (self.current_player + 1) % self.n_players
    

# Game start
# pick cards (is this going to be some combination of 5? for the AI)
# pick food
# pick bonus cards