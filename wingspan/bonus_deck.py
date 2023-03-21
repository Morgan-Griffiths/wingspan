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
    def __init__(self, name, expansion,automata,condition,explanitory_text,value_points,percent_birds):
        self.name = name
        self.expansion = expansion
        self.automata = automata
        self.condition = condition
        self.explanitory_text = explanitory_text
        self.value_points = value_points
        self.percent_birds = percent_birds

    def __str__(self):
        return f"\n{self.name}"
class Bonus:
    def __init__(self,minimum_birds,points):
        self.minimum_birds = minimum_birds
        self.points = points

class BonusCards:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)
    
    def discard(self, index):
        self.cards.pop(index)

    def __len__(self):
        return len(self.cards)

    def return_bonus_vector(self):
        return [card.name for card in self.cards]
    
class BonusDeck():
    def __init__(self):
        self.reset()
        

    def reset(self):
        self.cards = bonus_cards.copy()
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()