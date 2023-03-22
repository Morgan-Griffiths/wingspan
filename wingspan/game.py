from enum import Enum, auto
from wingspan.food import Food
from wingspan.helpers import UIState, human_readable_action_dictionary,action_dictionary, GameActions, IntermediateState
from wingspan.player import Player
from wingspan.shared import Shared
from wingspan.birds import WingspanBird
from wingspan.bonus_deck import BonusNames,bonus_name_dictionary_itos
import json
import numpy as np
class Game:
    def __init__(self, n_players, human_readable=True):
        self.n_players = n_players
        self.human_readable = human_readable
        self.shared = None
        self.players = None
        self.first_player = None
        self.discarding_cards = False
        self.discarding_food = False
        self.drawing_cards = False
        self.picking_food = False
        self.picking_bird = False
        self.picking_board_location = False
        self.birds = self.load_birds()

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
        self.first_player = self.current_player = self.shared.start_marker.position
        # set state
        self.state = UIState.initial_discard_cards
        # return initial observation
        action_vector = self.return_actions()
        return self.observation(),self.action_vector_to_readable(action_vector), 0, self.done

    @property
    def done(self):
        return self.state == UIState.game_over
    
    def increment_player(self):
        self.current_player = (self.current_player + 1) % self.n_players
    
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
    
    def return_actions(self):
        # construct action vector
        action_vector = np.zeros(len(human_readable_action_dictionary),dtype=int)
        if self.players[self.current_player].state == UIState.initial_discard_cards:
            hand_start = human_readable_action_dictionary['player hand one']
            num_cards = len(self.players[self.current_player].hand)
            action_vector[hand_start:hand_start+num_cards] = 1
            action_vector[human_readable_action_dictionary['no op']] = 1
        elif self.players[self.current_player].state == UIState.initial_discard_food:
            current_food = self.players[self.current_player].return_food_vector()
            food_start = human_readable_action_dictionary[Food.invertebrate]
            action_vector[food_start:food_start+5] = current_food
        elif self.players[self.current_player].state == UIState.initial_discard_bonus_cards:
            bonus_cards = self.players[self.current_player].return_bonus_card_vector()
            bonus_start = human_readable_action_dictionary['player bonus card one']
            action_vector[bonus_start:bonus_start+len(self.players[self.current_player].bonus_cards)] = bonus_cards
        elif self.players[self.current_player].state == UIState.round_1:
            # 4 actions
            action_start = human_readable_action_dictionary['play a bird']
            action_vector[action_start:action_start+4] = 1

            if self.players[self.current_player].can_discard_card_to_get_food():
                ...
            if self.shared.feeder.can_reroll():
                ...
        return action_vector
            
    def observation(self):
        return f'{self.state}\n' + f'{self.players[self.current_player].observation()}'

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
        elif self.players[self.current_player].state == UIState.round_1:
            # handle play bird card
            # handle lay eggs
            # handle draw cards
            # handle gain food
            if self.players[self.current_player].intermediate_state == IntermediateState.picking_feeder_food:
                # handle picking food, should be 1-5 + discard + reroll
                # check if they can discard a card to get food
                # if done revert intermediate state to None
                if action == 'discard':
                    # pick card to discard
                    self.players[self.current_player].intermediate_state = IntermediateState.picking_card_to_discard
                
                food = self.shared.pick_food(action)
                self.players[self.current_player].add_food(food)
                # if player is done with getting food, revert intermediate state to None (in future would check for bird activations)

                
            elif self.players[self.current_player].intermediate_state == IntermediateState.picking_card_to_draw:
                # handle picking card to draw
                # if done revert intermediate state to None
                self.players[self.current_player].draw_card(action)
            elif self.players[self.current_player].intermediate_state == IntermediateState.laying_eggs_on_bird:
                # choose bird to lay eggs on
                # if done revert intermediate state to None
                self.players[self.current_player].lay_eggs_on_bird(action)
            elif self.players[self.current_player].intermediate_state == IntermediateState.picking_bird_card_in_hand:
                
            elif self.players[self.current_player].intermediate_state == IntermediateState.picking_player_food:
                ...
            elif self.players[self.current_player].intermediate_state == IntermediateState.picking_bonus_card_to_keep:
                ...
            elif self.players[self.current_player].intermediate_state == IntermediateState.choosing_habitat_to_play_bird:
                ...
            elif self.players[self.current_player].intermediate_state == IntermediateState.choosing_bird_on_board:
                ...
            elif self.players[self.current_player].intermediate_state == IntermediateState.laying_eggs_on_bird:
                ...
            elif self.players[self.current_player].intermediate_state == IntermediateState.discarding_or_tucking_card_from_hand:
                ...
            if action == 'gain food':
                self.players[self.current_player].intermediate_state = IntermediateState.picking_feeder_food
            elif action == 'draw cards':
                self.players[self.current_player].intermediate_state = IntermediateState.picking_card_to_draw
            elif action == 'lay eggs':
                self.players[self.current_player].intermediate_state = IntermediateState.laying_eggs_on_bird
            elif action == 'play a bird':
                self.players[self.current_player].intermediate_state = IntermediateState.picking_bird_card_in_hand
            else:
                raise ValueError(f"Invalid action {action}")
            # check for round end. Distribute points across players, increment round
        elif self.players[self.current_player].state == UIState.round_2:
            ...
        elif self.players[self.current_player].state == UIState.round_3:
            ...
        elif self.players[self.current_player].state == UIState.round_4:
            ...
        action_vector = self.return_actions()
        return self.observation(),self.action_vector_to_readable(action_vector), 0, self.done

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


# Game start
# pick cards (is this going to be some combination of 5? for the AI)
# pick food
# pick bonus cards