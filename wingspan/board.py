import numpy as np
from wingspan.helpers import habitat_dict,Habitat

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


    def __bool__(self):
        return self.bird_card == None

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
    
    def is_habitat_available(self,habitat,n_eggs):
        row = habitat_dict[habitat]
        return bool(self.board[row][0] or (n_eggs > 0 and (self.board[row][1] or self.board[row][2])) or (n_eggs > 1 and (self.board[row][3] or self.board[row][4])))

    def can_discard_for_food(self):
        """ Check if the player can discard a card for food """
        return bool((self.board[0][0] is not None and self.board[0][1] is None) or (self.board[0][0:3] == True and self.board[0][3] is None) or (self.board[0][0:6] == True))

    def can_play_bird(self,card,n_eggs):
        """ Check if the bird can be played on the board """
        can_play = []
        for k,v in card.habitat.items():
            if v:
                can_play.append(self.is_habitat_available(k,n_eggs))
        return any(can_play)
        
    def add_bird_card(self, card, habitat, col):
        if habitat == Habitat.forest:
            row = 0
        elif habitat == Habitat.prairie:
            row = 1
        elif habitat == Habitat.wetlands:
            row = 2
        print(f'Adding bird card {card} to {row} {col}')
        self.board[row][col].add_bird_card(card)

    def add_eggs(self, eggs, row, col):
        self.board[row][col].add_eggs(eggs)

    def add_tucked_cards(self, cards, row, col):
        self.board[row][col].add_tucked_cards(cards)

    def remove_eggs(self, eggs, row, col):
        self.board[row][col].remove_eggs(eggs)

    def __repr__(self):
        return f'\n{self.board[0]} \n{self.board[1]} \n{self.board[2]}'