from enum import Enum, auto
from wingspan.food import Food
from wingspan.helpers import Habitat
import numpy as np



class FoodCost:
    def __init__(self, foods, one_of=False):
        self.foods = foods
        self.one_of = one_of

    def __str__(self):
        if self.one_of:
            return f'One of {self.foods}'
        else:
            return f'{self.foods}'


class NestType(Enum):
    """Enumerate all nest types in the game Wingspan."""

    bowl = auto()
    cavity = auto()
    platform = auto()
    ground = auto()
    star = auto()

    def __str__(self):
        return self.name


class ActivatedType(Enum):
    hunter = auto()
    flocking = auto()
    none = auto()

class WingspanBird:
    """Generic class for birds from the game Wingspan"""

    def __init__(
        self, name,action_type,power_category,power_text,predator,flocking,bonus_cards,points,nest_type,egg_capacity,wingspan,forest,wetlands,prairie,invertibrate,seed,fish,fruit,rodent,wild,or_food_cost,total_food_cost,bonuses
    ):
        self.name = name
        self.action_type = action_type
        self.power_category = power_category
        self.power_text = power_text
        self.predator = predator
        self.flocking = flocking
        self.bonus_cards = bonus_cards
        self.points = points
        self.nest_type = nest_type
        self.egg_capacity = egg_capacity
        self.wingspan = wingspan
        self.forest = forest
        self.wetlands = wetlands
        self.prairie = prairie
        self.invertibrate = invertibrate
        self.seed = seed
        self.fish = fish
        self.fruit = fruit
        self.rodent = rodent
        self.wild = wild
        self.or_food_cost = or_food_cost
        self.total_food_cost = total_food_cost
        self.eligible_bonuses = bonuses

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'\n\n{self.name} \nCost: \nWingspan: {self.wingspan} \nNest: {self.nest_type} \nEgg capacity: {self.egg_capacity} \nPoints: {self.points}'


def no_op_action():
    ...

# birds = [WingspanBird(*b) for b in raw_birds]