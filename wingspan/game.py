from enum import Enum, auto
from wingspan.food import Food
from wingspan.helpers import UIState, human_readable_action_dictionary, GameActions
from wingspan.player import Player
from wingspan.shared import Shared
from wingspan.birds import WingspanBird
from wingspan.bonus_deck import BonusNames
import json
import numpy as np
class Game:
    def __init__(self, n_players):
        self.n_players = n_players
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
            p.add_food(Food.invertibrate)
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
        self.first_player = self.shared.start_marker.position
        # set state
        self.state = UIState.initial_discard_cards
        # return initial observation
        return self.observation(),self.return_actions(), 0, self.done

    @property
    def done(self):
        return self.state == UIState.game_over
    
    def return_actions(self):
        # 3x5 vector for the board
        # 1x20 vector for the hand
        # 1x6 vector for the feeder
        # 1x2 vector for activating bird yes/no
        # 1x4 vector for drawing cards (3 faceup 1 deck)
        # vector for picking your food??
        # 15 + 20 + 6 + 2 + 4 = 47 length vector
        # construct action vector
        action_vector = np.zeros(58)
        if self.players[self.current_player].state == UIState.initial_discard_cards:
            hand_start = human_readable_action_dictionary['player food one']
            num_cards = len(self.players[self.current_player].hand)
            action_vector[hand_start:hand_start+num_cards] = 1
        elif self.players[self.current_player].state == UIState.initial_discard_food:
            current_food = self.players[self.current_player].return_food_vector()
            food_start = human_readable_action_dictionary['player food one']
            action_vector[food_start:food_start+5] = current_food
        elif self.players[self.current_player].state == UIState.initial_discard_bonus_cards:
            bonus_cards = self.players[self.current_player].return_bonus_card_vector()
        return action_vector
            
    def observation(self):
        return f'{self.state}\n' + f'{self.players[self.current_player].observation()}'

    def step(self, action):
        if self.players[self.current_player].state == UIState.initial_discard_cards:
            self.players[self.current_player].discard_bird_card(action)
        elif self.players[self.current_player].state == UIState.initial_discard_food:
            self.players[self.current_player].discard_food(action)
        elif self.players[self.current_player].state == UIState.initial_discard_bonus_cards:
            self.players[self.current_player].discard_bonus_card(action)
        elif self.players[self.current_player].state == UIState.round_1:
            ...

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