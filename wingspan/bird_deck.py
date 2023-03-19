from wingspan.birds import birds
from random import shuffle

class BirdDeck:
    def __init__(self):
        self.reset()

    def reset(self):
        self.cards = birds.copy()
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class DiscardDeck:
    def __init__(self):
        self.cards = []

    def discard(self, card):
        return self.cards.append(card)
