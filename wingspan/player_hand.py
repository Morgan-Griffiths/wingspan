class PlayerHand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def discard(self, index):
        self.cards.pop(index)

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)