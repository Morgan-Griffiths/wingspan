from wingspan.player import Player


class Game:
    def __init__(self, n_players):
        self.players = [Player() for _ in range(n_players)]
        self.reset()

    def reset(self):
        self.season = 0
        self.first_player = 0

    def step(self, action):
        ...

    def render(self):
        ...
