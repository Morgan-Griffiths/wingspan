from wingspan.birds import birds


class BirdDeck:
    def __init__(self):
        self.cards = birds.copy()

    def draw(self):
        return self.cards.pop()


class DiscardDeck:
    def __init__(self):
        self.cards = []

    def discard(self, card):
        return self.cards.append(card)
