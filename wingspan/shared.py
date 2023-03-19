from wingspan.bird_deck import BirdDeck
from wingspan.bird_faceup import BirdFaceup
from wingspan.bonus_deck import BonusDeck
from wingspan.feeder import Feeder
from wingspan.goals import Goals


class Shared:
    def __init__(self):
        self.feeder = Feeder()
        self.goals = Goals()
        self.birds = BirdDeck()
        self.bonuses = BonusDeck()
        self.discards = BirdDeck()
        self.faceup = BirdFaceup()