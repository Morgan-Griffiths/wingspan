class BirdFaceup:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def reset(self):
        self.cards = []