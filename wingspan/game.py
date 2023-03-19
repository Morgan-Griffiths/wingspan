from enum import Enum, auto
from wingspan.food import Food
from wingspan.player import Player
from wingspan.shared import Shared
from wingspan.birds import birds

from random import shuffle


class UIState(Enum):
    initial_discard = auto()
    round_1 = auto()
    round_2 = auto()
    round_3 = auto()
    round_4 = auto()
    game_over = auto()


class Game:
    def __init__(self, n_players):
        self.state = UIState.initial_discard
        self.shared = Shared()
        self.players = [Player() for _ in range(n_players)]
        self.season = 0
        self.n_players = n_players
        self.first_player = 0
        self.current_player = 0

    def reset(self):
        self.season = 0
        self.first_player = 0
        shuffle(birds)
        self.deck = birds
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
            
    def step(self, action):
        ...

    def render(self):
        self.shared.render()
        for player in self.players:
            player.render()

    def play(self):
        if self.state == UIState.game_over:
            print("Game over")
            return
        elif self.state == UIState.initial_discard:
            card_names = [
                f"{i} {c.name}"
                for i, c in enumerate(self.players[self.current_player].hand)
            ]
            print(
                f"Current player: {self.current_player} discard cards: {', '.join(card_names)}"
            )
            self.state = UIState.game_over
