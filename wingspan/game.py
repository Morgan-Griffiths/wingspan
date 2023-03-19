from enum import Enum, auto
from wingspan.player import Player
from wingspan.shared import Shared


class UIState(Enum):
    initial_discard = auto()
    game_over = auto()


class Game:
    def __init__(self, n_players):
        self.state = UIState.initial_discard
        self.shared = Shared()
        self.players = [Player(self.shared.birds) for _ in range(n_players)]
        self.season = 0
        self.first_player = 0
        self.current_player = 0

    def reset(self):
        self.season = 0
        self.first_player = 0

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
