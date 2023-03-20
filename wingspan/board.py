import numpy as np
from wingspan.birds import Habitat

class Square:
    def __init__(self, habitat):
        self.habitat = habitat
        self.eggs = 0
        self.tucked_cards = 0
        self.bird_card = None

    def add_bird_card(self, card):
        self.bird_card = card
    
    def add_eggs(self, eggs):
        self.eggs += eggs

    def add_tucked_cards(self, cards):
        self.tucked_cards += cards

    def remove_eggs(self, eggs):
        self.eggs -= eggs

    def __repr__(self):
        return f'{self.habitat} {self.eggs} {self.tucked_cards} {self.bird_card}'

class Board():
    def __init__(self):
        """ 3x5 board """
        self.board = [
            [Square(Habitat.forest), Square(Habitat.forest), Square(Habitat.forest), Square(Habitat.forest), Square(Habitat.forest)],
            [Square(Habitat.prairie), Square(Habitat.prairie), Square(Habitat.prairie), Square(Habitat.prairie), Square(Habitat.prairie)],
            [Square(Habitat.wetlands), Square(Habitat.wetlands), Square(Habitat.wetlands), Square(Habitat.wetlands), Square(Habitat.wetlands)]
        ]
        
    def add_bird_card(self, card, row, col):
        self.board[row][col].add_bird_card(card)

    def add_eggs(self, eggs, row, col):
        self.board[row][col].add_eggs(eggs)

    def add_tucked_cards(self, cards, row, col):
        self.board[row][col].add_tucked_cards(cards)

    def remove_eggs(self, eggs, row, col):
        self.board[row][col].remove_eggs(eggs)

    def __repr__(self):
        return f'\n{self.board[0]} \n{self.board[1]} \n{self.board[2]}'