from wingspan.board import Board
from wingspan.bonus_deck import BonusCards
from wingspan.helpers import UIState,player_hand_dictionary_stoi,player_food_dictionary_stoi,player_bonus_card_dictionary_stoi,IntermediateState
from wingspan.player_food import PlayerFood
from wingspan.player_hand import PlayerHand
from wingspan.helpers import GameActions


class Player:
    def __init__(self):
        self.tucked = 0
        self.cached = 0
        self.eggs = 0
        self.hand = PlayerHand()
        self.bonus_cards = BonusCards()
        self.board = Board()
        self.food = PlayerFood()
        self.state = UIState.initial_discard_cards
        self.intermediate_state = IntermediateState.no_op
        self.turn = 0

    def reset(self):
        ...

    def increment_turn(self):
        self.turn += 1

    def reset_turn(self):
        self.turn = 0

    def pick_food(self):
        ...

    def can_discard_card_to_get_food(self):
        return self.board.can_discard_for_food()

    def add_bird_cards(self, cards):
        for card in cards:
            self.hand.add(card)

    def add_bird_card(self, card):
        self.hand.add(card)

    def add_bonus_card(self,card):
        self.bonus_cards.add(card)

    def discard_bonus_card(self,index):
        self.bonus_cards.discard(index)

    def add_food(self,food):
        self.food.add(food)

    def return_food_vector(self):
        return self.food.return_food_vector()
    
    def return_bonus_card_vector(self):
        return self.bonus_cards.return_bonus_card_vector()

    def discard_food(self,food):
        self.food.discard(food)

    def discard_bird_card(self, action):
        if self.state == UIState.initial_discard_cards:
            if action == GameActions.no_op: # discard is over
                self.state = UIState.initial_discard_food
                return
            else:
                index = player_hand_dictionary_stoi[action]
                self.hand.discard(index)
        elif self.state == UIState.initial_discard_food:
            # compare num food vs num cards
            index = player_hand_dictionary_stoi[action]
            self.food.discard(index)
            if len(self.hand) - 5 == len(self.food):
                self.state = UIState.initial_discard_bonus_cards
        elif self.state == UIState.initial_discard_bonus_cards:
            index = player_bonus_card_dictionary_stoi[action]
            self.discard_bonus_card(index)
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
            return self.return_food_vector(),
        elif self.state == UIState.initial_discard_bonus_cards:
            return f"bonus_cards: {self.bonus_cards}",
        return {
            "tucked": self.tucked,
            "cached": self.cached,
            "hand": [card for card in self.hand.cards],
            "bonus_cards": self.bonus_cards,
            "board": self.board,
            "food": self.food,
            "turn": self.turn,
        }
    

    def play_bird_card(self, action):
        ...

    def gain_food(self, food):
        ...

    def render(self):
        print(f"tucked/cached={self.tucked+self.cached}")
        for card in self.hand:
            print(card)
        for card in self.bonus_cards:
            print(card)
        self.food.render()

    def can_play_bird(self):
        can_play = False
        for card in self.hand:
            # if you have the food to play the card
            # if there is space on the board
            if card in self.food:
                if self.board.can_play(card,self.eggs):
                    can_play = True
                    break
        return can_play