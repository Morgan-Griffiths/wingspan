from enum import Enum

class FoodCost:
    def __init__(self,n_invertibrates,n_seeds,n_fish,n_mouse,n_berry,n_wild):
        self.n_invertibrates = n_invertibrates
        self.n_seeds = n_seeds
        self.n_fish = n_fish
        self.n_mouse = n_mouse
        self.n_berry = n_berry
        self.n_wild = n_wild

class NestType(Enum):
    """ Enumerate all nest types in the game Wingspan. """
    bowl = 1
    cavity = 2
    platform = 3
    ground = 4
    star = 5

class ActivatedType(Enum):
    hunter = 1
    flocking = 2
    none = 3


class WingspanBird:
    """ Generic class for birds from the game Wingspan """
    def __init__(self,n_invertibrates,n_seeds,n_fish,n_mouse,n_berry,n_wild,wingspan,nest_type,egg_capacity,points,action):
        self.food_cost = FoodCost(n_invertibrates,n_seeds,n_fish,n_mouse,n_berry,n_wild)
        self.wingspan = wingspan
        self.nest_type = nest_type
        self.egg_capacity = egg_capacity
        self.points = points
        self.action = action

""" Enumerate all 170 birds in the game Wingspan. """

eastern_screech_owl = WingspanBird(1,1,1,1,1)
belted_kingfisher = WingspanBird(1,1,1,1,1)