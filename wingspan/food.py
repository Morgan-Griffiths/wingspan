from enum import Enum, auto


class Food(Enum):
    invertibrate = auto()
    seed = auto()
    fruit = auto()
    rodent = auto()
    fish = auto()
    wild = auto()

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name