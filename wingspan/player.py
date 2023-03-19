from wingspan.board import Board
from wingspan.player_food import PlayerFood


class Player:
    def __init__(self, bird_deck):
        self.tucked = 0
        self.cached = 0
        self.hand = [bird_deck.draw() for _ in range(5)]
        self.bonus_cards = []
        self.board = Board()
        self.food = PlayerFood()

    def render(self):
        print(f"tucked/cached={self.tucked+self.cached}")
        for card in self.hand:
            print(card)
