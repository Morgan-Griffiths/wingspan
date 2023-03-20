from enum import auto
from random import shuffle

class BonusNames:
    Anatomist = auto()
    Cartographer = auto()
    Historian = auto()
    Photographer = auto()
    Backyard_Birder = auto()
    Bird_Bander = auto()
    Bird_Counter = auto()
    Bird_Feeder = auto()
    Diet_Specialist = auto()
    Enclosure_Builder = auto()
    Falconer = auto()
    Fishery_Manager = auto()
    Food_Web_Expert = auto()
    Forester = auto()
    Large_Bird_Specialist = auto()
    Nest_Box_Builder = auto()
    Omnivore_Expert = auto()
    Passerine_Specialist = auto()
    Platform_Builder = auto()
    Prairie_Manager = auto()
    Rodentologist = auto()
    Viticulturalist = auto()
    Wetland_Scientist = auto()
    Wildlife_Gardener = auto()
    
class BonusCard:
    def __init__(self, name, stage1,stage2, rules=None):
        self.name = name
        self.stage1 = stage1
        self.stage2 = stage2
        self.rules = rules

    def __str__(self):
        return f"\n{self.name}"
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