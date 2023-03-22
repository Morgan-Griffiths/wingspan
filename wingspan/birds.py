from enum import Enum, auto
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
        self, name,action,points,nest_type,egg_capacity,wingspan,habitat,food_cost,bonuses
    ):
        self.name = name
        self.action = action
        self.points = points
        self.nest_type = nest_type
        self.egg_capacity = egg_capacity
        self.habitat = habitat
        self.food_cost = food_cost
        self.bonuses = bonuses
        self.wingspan = wingspan

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'\n\n{self.name} \nCost: {self.food_cost} \nWingspan: {self.wingspan} \nNest: {self.nest_type} \nEgg capacity: {self.egg_capacity} \nPoints: {self.points}'


def no_op_action():
    ...

# birds = [WingspanBird(*b) for b in raw_birds]