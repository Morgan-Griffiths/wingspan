from wingspan.board import Board
from wingspan.bonus_deck import BonusCards
from wingspan.helpers import UIState
from wingspan.player_food import PlayerFood
from wingspan.player_hand import PlayerHand
from wingspan.helpers import GameActions


class Player:
    def __init__(self):
        self.tucked = 0
        self.cached = 0
        self.hand = PlayerHand()
        self.bonus_cards = BonusCards()
        self.board = Board()
        self.food = PlayerFood()
        self.state = UIState.initial_discard_cards
        self.turn = 0

    def reset(self):
        ...

    def increment_turn(self):
        self.turn += 1

    def reset_turn(self):
        self.turn = 0

    def add_bird_cards(self, cards):
        for card in cards:
            self.hand.add(card)

    def add_bird_card(self, card):
        self.hand.add(card)

    def add_bonus_card(self,card):
        self.bonus_cards.add(card)

    def discard_bonus_card(self,action):
        self.bonus_cards.discard(action)

    def add_food(self,food):
        self.food.add(food)

    def discard_food(self,food):
        self.food.discard(food)

    def discard_bird_card(self, action):
        if self.state == UIState.initial_discard_cards:
            if action == GameActions.no_op: # discard is over
                self.state = UIState.initial_discard_food
                return
            else:
                self.hand.discard(action)
        elif self.state == UIState.initial_discard_food:
            # compare num food vs num cards
            self.food.discard(action)
            if len(self.hand) - 5 == len(self.food):
                self.state = UIState.initial_discard_bonus_cards
        elif self.state == UIState.initial_discard_bonus_cards:
            self.discard_bonus_card(action)
            self.state = UIState.round_1
        elif self.state == UIState.round_1:
            ...


    def cache_bird_card(self, card):
        self.hand.discard(card)
        self.cached += 1



    def observation(self):
        if self.state == UIState.initial_discard_cards:
            return f"hand {[card for card in self.hand.cards]}"
        elif self.state == UIState.initial_discard_food:
            return {"food": [food for food in self.food]},
        elif self.state == UIState.initial_discard_bonus_cards:
            return {"bonus_cards": [card for card in self.bonus_cards]},
        return {
            "tucked": self.tucked,
            "cached": self.cached,
            "hand": [card for card in self.hand.cards],
            "bonus_cards": [card for card in self.bonus_cards],
            "board": self.board,
            "food": self.food,
            "turn": self.turn,
        }

    def render(self):
        print(f"tucked/cached={self.tucked+self.cached}")
        for card in self.hand:
            print(card)
        for card in self.bonus_cards:
            print(card)
        self.food.render()