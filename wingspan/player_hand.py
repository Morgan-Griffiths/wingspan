class PlayerHand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def discard(self, card):
        self.cards.remove(card)