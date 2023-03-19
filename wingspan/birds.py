from enum import Enum, auto
from wingspan.food import Food


class FoodCost:
    def __init__(self, n_invertibrates, n_seeds, n_fish, n_rodent, n_fruit, n_wild):
        self.n_invertibrates = n_invertibrates
        self.n_seeds = n_seeds
        self.n_fish = n_fish
        self.n_rodent = n_rodent
        self.n_fruit = n_fruit
        self.n_wild = n_wild


class NestType(Enum):
    """Enumerate all nest types in the game Wingspan."""

    bowl = 1
    cavity = 2
    platform = 3
    ground = 4
    star = 5


class ActivatedType(Enum):
    hunter = 1
    flocking = 2
    none = 3


class Habitat(Enum):
    forest = auto()
    prairie = auto()
    wetlands = auto()


class WingspanBird:
    """Generic class for birds from the game Wingspan"""

    def __init__(
        self, name, habitat, foodcost, wingspan, nest_type, egg_capacity, points, action
    ):
        self.name = name
        self.habitat = habitat
        self.food_cost = foodcost
        self.wingspan = wingspan
        self.nest_type = nest_type
        self.egg_capacity = egg_capacity
        self.points = points
        self.action = action


""" Enumerate all 170 birds in the game Wingspan. """

eastern_screech_owl = WingspanBird(1, 1, 1, 1, 1)
belted_kingfisher = WingspanBird(1, 1, 1, 1, 1)


def no_op_action():
    ...


birds = [
    WingspanBird(
        name="Wood Duck",
        habitat={Habitat.wetlands, Habitat.forest},
        foodcost=FoodCost([Food.seed, Food.seed, Food.fruit], one_of=False),
        wingspan=76,
        nest_type=NestType.cavity,
        egg_capacity=4,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        name="Belted Kingfisher",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.wild], one_of=False),
        wingspan=53,
        nest_type=NestType.star,
        egg_capacity=4,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        name="Abbot's booby",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.fish], one_of=False),
        wingspan=190,
        nest_type=NestType.platform,
        egg_capacity=1,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "Acorn Woodpecker",
        habitat={Habitat.forest},
        foodcost=FoodCost([Food.seed, Food.seed, Food.seed], one_of=False),
        wingspan=46,
        nest_type=NestType.cavity,
        egg_capacity=4,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "American Avocet",
        habitat={Habitat.wetlands},
        foodcost=FoodCost(2, 1, 0, 0, 0, 0),
        wingspan=79,
        nest_type=NestType.ground,
        egg_capacity=2,
        points=6,
        action=no_op_action,
    ),
    WingspanBird(
        "American Bittern",
        habitat={Habitat.wetlands},
        foodcost=FoodCost(1, 0, 1, 1, 0, 0),
        wingspan=107,
        nest_type=NestType.platform,
        egg_capacity=2,
        points=7,
        action=no_op_action,
    ),
    WingspanBird(
        "American coot",
        foodcost=FoodCost(0, 1, 0, 0, 0, 1),
        wingspan=61,
        nest_type=NestType.platform,
        egg_capacity=5,
        points=3,
        action=no_op_action,
    ),
    WingspanBird(
        "American Crow",
        foodcost=FoodCost(0, 0, 0, 0, 0, 1),
        wingspan=99,
        nest_type=NestType.platform,
        egg_capacity=2,
    ),
]
