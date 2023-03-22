from enum import Enum, auto
from random import shuffle
import json


class BonusNames(Enum):
    Anatomist = auto()
    Backyard_Birder = auto()
    Bird_Counter = auto()
    Bird_Feeder = auto()
    Breeding_Manager = auto()
    Cartographer = auto()
    Ecologist = auto()
    Enclosure_Builder = auto()
    Falconer = auto()
    Fishery_Manager = auto()
    Food_Web_Expert = auto()
    Forester = auto()
    Historian = auto()
    Large_Bird_Specialist = auto()
    Nest_Box_Builder = auto()
    Omnivore_Specialist = auto()
    Oologist = auto()
    Passerine_Specialist = auto()
    Photographer = auto()
    Platform_Builder = auto()
    Prairie_Manager = auto()
    Rodentologist = auto()
    Visionary_Leader = auto()
    Viticulturalist = auto()
    Wetland_Scientist = auto()
    Wildlife_Gardener = auto()


bonus_name_dictionary_stoi = {
    'Anatomist': BonusNames.Anatomist,
    'Backyard Birder': BonusNames.Backyard_Birder,
    'Bird Counter': BonusNames.Bird_Counter,
    'Bird Feeder': BonusNames.Bird_Feeder,
    'Breeding Manager': BonusNames.Breeding_Manager,
    'Cartographer': BonusNames.Cartographer,
    'Ecologist': BonusNames.Ecologist,
    'Enclosure Builder': BonusNames.Enclosure_Builder,
    'Falconer': BonusNames.Falconer,
    'Fishery Manager': BonusNames.Fishery_Manager,
    'Food Web Expert': BonusNames.Food_Web_Expert,
    'Forester': BonusNames.Forester,
    'Historian': BonusNames.Historian,
    'Large Bird Specialist': BonusNames.Large_Bird_Specialist,
    'Nest Box Builder': BonusNames.Nest_Box_Builder,
    'Omnivore Specialist': BonusNames.Omnivore_Specialist,
    'Oologist': BonusNames.Oologist,
    'Passerine Specialist': BonusNames.Passerine_Specialist,
    'Photographer': BonusNames.Photographer,
    'Platform Builder': BonusNames.Platform_Builder,
    'Prairie Manager': BonusNames.Prairie_Manager,
    'Rodentologist': BonusNames.Rodentologist,
    'Visionary Leader': BonusNames.Visionary_Leader,
    'Viticulturalist': BonusNames.Viticulturalist,
    'Wetland Scientist': BonusNames.Wetland_Scientist,
    'Wildlife Gardener': BonusNames.Wildlife_Gardener,
}

bonus_name_dictionary_itos = { v.value: k for k, v in bonus_name_dictionary_stoi.items() }
bonus_name_dictionary_itos[0] = '<PAD>'
    
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
    
    def __repr__(self):
        return f"\n{self.name}, {self.condition}, {self.explanitory_text}, points: {self.value_points}, % of birds: {self.percent_birds}"
class Bonus:
    def __init__(self,minimum_birds,points):
        self.minimum_birds = minimum_birds
        self.points = points

class BonusCards:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)
    
    def discard(self, name):
        index = [i for i, card in enumerate(self.cards) if card.name == name][0]
        self.cards.pop(index)

    def return_bonus_card_vector(self):
        return [bonus_name_dictionary_stoi[card.name].value for card in self.cards]
    
    def __len__(self):
        return len(self.cards)
    
    def __repr__(self):
        return f"{self.cards}"
    
class BonusDeck():
    def __init__(self):
        with open('bonus_cards.json', 'r') as f:
            bonus_cards = json.loads(f.read())
        self.bonus_cards = [BonusCard(**b) for b in bonus_cards]
        # print(self.bonus_cards)
        self.reset()
        
    def reset(self):
        self.cards = self.bonus_cards.copy()
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def __repr__(self):
        return f"{self.cards}"