from wingspan.bird_deck import BirdDeck, DiscardDeck
from wingspan.bird_faceup import BirdFaceup
from wingspan.bonus_deck import BonusDeck
from wingspan.feeder import Feeder
from wingspan.goals import Goals
from wingspan.marker import Marker

import random

class Shared:
    def __init__(self,birds):
        self.feeder = Feeder()
        self.goals = Goals()
        self.birds = BirdDeck(birds)
        self.bonuses = BonusDeck()
        self.discards = DiscardDeck()
        self.faceup = BirdFaceup()
        self.start_marker = Marker()

    def render(self):
        print("shared")

    def draw_bird_card(self):
        return self.birds.draw()
    
    def draw_bonus_card(self):
        return self.bonuses.draw()

    def place_start_marker(self,n_players):
        self.start_marker.place(random.randint(0, n_players - 1))