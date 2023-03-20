
from enum import Enum, auto


class UIState(Enum):
    initial_discard_cards = auto()
    initial_discard_food = auto()
    initial_discard_bonus_cards = auto()
    round_1 = auto()
    round_2 = auto()
    round_3 = auto()
    round_4 = auto()
    game_over = auto()

    def __repr__(self) -> str:
        return self.name
    

class Habitat(Enum):
    forest = auto()
    prairie = auto()
    wetlands = auto()

class PowerCategories(Enum):
    caching_food = auto()
    egg_laying = auto()
    card_drawing = auto()
    flocking = auto()
    food_from_supply = auto()
    hunting_fishing = auto()
    food_from_birdfeeder = auto()
    other = auto()

class PowerColors(Enum):
    brown = auto()
    pink = auto()
    white = auto()






