from wingspan.board import Board
from wingspan.helpers import UIState
from wingspan.player_food import PlayerFood
from wingspan.player_hand import PlayerHand


class Player:
    def __init__(self):
        self.tucked = 0
        self.cached = 0
        self.hand = PlayerHand()
        self.bonus_cards = []
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
        self.bonus_cards.append(card)

    def add_food(self,food):
        self.food.add(food)

    def discard_bonus_card(self,card):
        self.bonus_cards.remove(card)

    def cache_bird_card(self, card):
        self.hand.discard(card)
        self.cached += 1

    def cache_food(self,food):
        ...

    def discard_bird_card(self, card):
        self.hand.add(card)

    def observation(self):
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