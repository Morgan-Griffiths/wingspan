

class Player:
    def __init__(self):
        self.score = 0
        self.hand = []
        self.bonus_cards = []
        self.board = []
        self.eggs = []
        self.food = []

class Wingspan:
    def __init__(self,n_players):
        self.n_players = n_players
        self.reset()

    def reset(self):
        ...

    def step(self,action):
        ...

    def render(self):
        ...