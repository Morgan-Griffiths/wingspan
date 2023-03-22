from enum import Enum, auto


class Food(Enum):
    invertebrate = auto()
    seed = auto()
    fruit = auto()
    rodent = auto()
    fish = auto()
    wild = auto()

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
food_name_dictionary = {
    'invertebrate': Food.invertebrate,
    'seed': Food.seed,
    'fruit': Food.fruit,
    'rodent': Food.rodent,
    'fish': Food.fish,
    'wild': Food.wild,
}