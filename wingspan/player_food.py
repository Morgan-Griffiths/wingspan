from enum import Enum, auto

class FoodType(Enum):
    invertibrate = auto()
    seed = auto()
    fruit = auto()
    rodent = auto()
    fish = auto()

class PlayerFood():
    def __init__(self):
        self.food = [0,0,0,0,0]
