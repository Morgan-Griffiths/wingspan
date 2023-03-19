from wingspan.board import Board
from wingspan.player_food import PlayerFood


class Player:
    def __init__(self):
        self.tucked = 0
        self.cached = 0
        self.hand = []
        self.bonus_cards = []
        self.board = Board()
        self.food = PlayerFood()