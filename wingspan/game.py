class Game:
    def __init__(self,n_players):
        self.n_players = n_players
        self.reset()

    def reset(self):
        ...

    def step(self,action):
        ...

    def render(self):
        ...