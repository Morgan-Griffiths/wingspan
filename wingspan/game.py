from enum import Enum, auto
from wingspan.food import Food
from wingspan.helpers import UIState
from wingspan.player import Player
from wingspan.shared import Shared
from wingspan.birds import WingspanBird
from wingspan.bonus_deck import BonusNames
import pickle

class Game:
    def __init__(self, n_players):
        self.n_players = n_players
        self.shared = None
        self.players = None
        self.first_player = None
        self.birds = self.load_birds()

    def load_birds(self):
        with open('birds.pkl', 'rb') as f:
            raw_birds = pickle.load(f)

        birds = []
        bonus_names = [x.lower() for x in filter(lambda x: x[0] != '_',dir(BonusNames))]
        print(bonus_names)
        for raw_bird in raw_birds:
            print(raw_bird)
            # enumerate the BonusNames
            bonus_vector = [raw_bird[name] for name in bonus_names]
            for name in bonus_names:
                del raw_bird[name]
            
            
            birds.append(WingspanBird(*raw_bird, bonus_vector))


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
        self.current_player = self.shared.start_marker.position
        # set state
        self.state = UIState.initial_discard_cards
        # return initial observation
        return self.observation(), 0, self.done

    @property
    def done(self):
        return self.state == UIState.game_over
            
    def observation(self):
        return f'{self.state}\n' + f'{self.players[self.current_player].observation()}'

    def step(self, action):
        if self.players[self.current_player].state == UIState.initial_discard_cards:
            self.players[self.current_player].discard_bird_card(action)
            self.players[self.current_player].state = UIState.initial_discard_food
        elif self.players[self.current_player].state == UIState.initial_discard_food:
            self.players[self.current_player].discard_food(action)
            self.players[self.current_player].state = UIState.initial_discard_bonus_cards
        elif self.players[self.current_player].state == UIState.initial_discard_bonus_cards:
            self.players[self.current_player].discard_bonus_card(action)
            self.players[self.current_player].state = UIState.round_1
            # start at marker
            self.current_player = self.shared.start_marker.position
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