from random import shuffle

class BonusCard:
    def __init__(self, name, stage1,stage2, rules=None):
        self.name = name
        self.stage1 = stage1
        self.stage2 = stage2
        self.rules = rules

class Bonus:
    def __init__(self,minimum_birds,points):
        self.minimum_birds = minimum_birds
        self.points = points

bonus_cards = [
    BonusCard("Anatomist", Bonus(2,3),Bonus(4,7)),
    BonusCard('Avian Theriogenologist', Bonus(5,4),Bonus(7,7)),
    BonusCard('Backyard Birder', Bonus(5,3),Bonus(7,6)),
    BonusCard('Bird Counter', Bonus(5,4),None), # 2 per bird
]
class BonusDeck():
    def __init__(self):
        self.reset()

    def reset(self):
        self.cards = bonus_cards.copy()
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()