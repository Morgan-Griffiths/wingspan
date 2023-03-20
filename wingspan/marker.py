class Marker:
    def __init__(self):
        self.marker = None

    def place(self, player):
        self.marker = player

    def increment(self, players):
        self.marker = (self.marker + 1) % len(players)

    @property
    def position(self):
        return self.marker