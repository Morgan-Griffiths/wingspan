class Game:
    def __init__(self,n_players):
        self.n_players = n_players
        self.reset()

    def reset(self):
        self.season = 0
        self.first_player = 0

    def step(self,action):
        ...

    def render(self):
        ...