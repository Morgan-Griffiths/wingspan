from enum import Enum, auto
from wingspan.food import Food


class FoodCost:
    def __init__(self, foods, one_of=False):
        self.foods = foods
        self.one_of = one_of


class NestType(Enum):
    """Enumerate all nest types in the game Wingspan."""

    bowl = auto()
    cavity = auto()
    platform = auto()
    ground = auto()
    star = auto()


class ActivatedType(Enum):
    hunter = auto()
    flocking = auto()
    none = auto()


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

    def __str__(self):
        return self.name


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
        foodcost=FoodCost(
            [Food.invertibrate, Food.invertibrate, Food.seed], one_of=False
        ),
        wingspan=79,
        nest_type=NestType.ground,
        egg_capacity=2,
        points=6,
        action=no_op_action,
    ),
    WingspanBird(
        "American Bittern",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.invertibrate, Food.fish, Food.rodent], one_of=False),
        wingspan=107,
        nest_type=NestType.platform,
        egg_capacity=2,
        points=7,
        action=no_op_action,
    ),
    WingspanBird(
        "American coot",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.seed, Food.wild], one_of=False),
        wingspan=61,
        nest_type=NestType.platform,
        egg_capacity=5,
        points=3,
        action=no_op_action,
    ),
    WingspanBird(
        "American Crow",
        habitat={Habitat.wetlands, Habitat.prairie, Habitat.forest},
        foodcost=FoodCost([Food.wild], one_of=False),
        wingspan=99,
        nest_type=NestType.platform,
        egg_capacity=2,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "American Goldfinch",
        habitat={Habitat.prairie},
        foodcost=FoodCost([Food.seed, Food.seed]),
        wingspan=23,
        nest_type=NestType.bowl,
        egg_capacity=3,
        points=3,
        action=no_op_action,
    ),
    WingspanBird(
        "American Kestrel",
        habitat={Habitat.prairie},
        foodcost=FoodCost([Food.invertibrate, Food.rodent]),
        wingspan=56,
        nest_type=NestType.cavity,
        egg_capacity=3,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "American Oystercatcher",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.invertibrate, Food.invertibrate]),
        wingspan=81,
        nest_type=NestType.ground,
        egg_capacity=2,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "American Redstart",
        habitat={Habitat.forest},
        foodcost=FoodCost([Food.invertibrate, Food.fruit]),
        wingspan=20,
        nest_type=NestType.bowl,
        egg_capacity=2,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "American Robin",
        habitat={Habitat.forest, Habitat.prairie},
        foodcost=FoodCost([Food.invertibrate, Food.fruit], one_of=True),
        wingspan=43,
        nest_type=NestType.bowl,
        egg_capacity=4,
        points=1,
        action=no_op_action,
    ),
    WingspanBird(
        "American White Pelican",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.fish], one_of=False),
        wingspan=274,
        nest_type=NestType.ground,
        egg_capacity=1,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "American Woodcock",
        habitat={Habitat.prairie, Habitat.forest},
        foodcost=FoodCost(
            [Food.invertibrate, Food.invertibrate, Food.seed], one_of=False
        ),
        wingspan=46,
        nest_type=NestType.ground,
        egg_capacity=2,
        points=9,
        action=no_op_action,
    ),
    WingspanBird(
        "Anhinga",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.fish], one_of=False),
        wingspan=114,
        nest_type=NestType.platform,
        egg_capacity=2,
        points=6,
        action=no_op_action,
    ),
    WingspanBird(
        "Anna's Hummingbird",
        habitat={Habitat.wetlands, Habitat.forest, Habitat.prairie},
        foodcost=FoodCost([Food.wild], one_of=False),
        wingspan=13,
        nest_type=NestType.bowl,
        egg_capacity=2,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "Ash-throated Flycatcher",
        habitat={Habitat.prairie},
        foodcost=FoodCost(
            [Food.invertibrate, Food.invertibrate, Food.fruit], one_of=False
        ),
        wingspan=30,
        nest_type=NestType.cavity,
        egg_capacity=4,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "Atlantic Puffin",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.fish, Food.fish], one_of=False),
        wingspan=53,
        nest_type=NestType.star,
        egg_capacity=1,
        points=8,
        action=no_op_action,
    ),
    WingspanBird(
        "Anduuin's Gull",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.wild], one_of=False),
        wingspan=132,
        nest_type=NestType.ground,
        egg_capacity=2,
        points=1,
        action=no_op_action,
    ),
    WingspanBird(
        "Australian Shoveler",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.invertibrate, Food.seed], one_of=False),
        wingspan=75,
        nest_type=NestType.ground,
        egg_capacity=4,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "Australian Ibis",
        habitat={Habitat.wetlands, Habitat.prairie},
        foodcost=FoodCost([Food.invertibrate, Food.fish, Food.wild], one_of=False),
        wingspan=118,
        nest_type=NestType.platform,
        egg_capacity=2,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "Baird's Sparrow",
        habitat={Habitat.prairie},
        foodcost=FoodCost([Food.invertibrate, Food.seed], one_of=False),
        wingspan=23,
        nest_type=NestType.ground,
        egg_capacity=2,
        points=3,
        action=no_op_action,
    ),
    WingspanBird(
        "Bald Eagle",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.fish, Food.rodent], one_of=False),
        wingspan=203,
        nest_type=NestType.platform,
        egg_capacity=1,
        points=9,
        action=no_op_action,
    ),
    WingspanBird(
        "Baltimore Oriole",
        habitat={Habitat.forest},
        foodcost=FoodCost([Food.invertibrate, Food.fruit, Food.fruit], one_of=False),
        wingspan=30,
        nest_type=NestType.star,
        egg_capacity=2,
        points=9,
        action=no_op_action,
    ),
    WingspanBird(
        "Barn owl",
        habitat={Habitat.prairie, Habitat.wetlands, Habitat.forest},
        foodcost=FoodCost([Food.rodent, Food.rodent], one_of=False),
        wingspan=107,
        nest_type=NestType.cavity,
        egg_capacity=4,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "Barn Swallow",
        habitat={Habitat.prairie, Habitat.wetlands},
        foodcost=FoodCost([Food.invertibrate], one_of=False),
        wingspan=38,
        nest_type=NestType.star,
        egg_capacity=3,
        points=1,
        action=no_op_action,
    ),
    WingspanBird(
        "Barred owl",
        habitat={Habitat.forest},
        foodcost=FoodCost([Food.rodent], one_of=False),
        wingspan=107,
        nest_type=NestType.cavity,
        egg_capacity=2,
        points=3,
        action=no_op_action,
    ),
    WingspanBird(
        "Barrow's Goldeneye",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.invertibrate, Food.seed, Food.fish], one_of=False),
        wingspan=71,
        nest_type=NestType.cavity,
        egg_capacity=4,
        points=5,
        action=no_op_action,
    ),
    WingspanBird(
        "Bell's Vireo",
        habitat={Habitat.prairie, Habitat.forest},
        foodcost=FoodCost([Food.invertibrate, Food.invertibrate], one_of=False),
        wingspan=18,
        nest_type=NestType.star,
        egg_capacity=2,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "Bewick's Wren",
        habitat={Habitat.prairie, Habitat.wetlands, Habitat.forest},
        foodcost=FoodCost(
            [Food.invertibrate, Food.invertibrate, Food.seed], one_of=False
        ),
        wingspan=18,
        nest_type=NestType.cavity,
        egg_capacity=3,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "Black Skimmer",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.fish, Food.fish], one_of=False),
        wingspan=112,
        nest_type=NestType.ground,
        egg_capacity=2,
        points=6,
        action=no_op_action,
    ),
    WingspanBird(
        "Black Tern",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.invertibrate, Food.fish], one_of=True),
        wingspan=61,
        nest_type=NestType.star,
        egg_capacity=2,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "Black Vulture",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([], one_of=False),
        wingspan=150,
        nest_type=NestType.cavity,
        egg_capacity=1,
        points=2,
        action=no_op_action,
    ),
    WingspanBird(
        "Black woodpecker",
        habitat={Habitat.forest},
        foodcost=FoodCost(
            [Food.invertibrate, Food.invertibrate, Food.fruit], one_of=False
        ),
        wingspan=70,
        nest_type=NestType.cavity,
        egg_capacity=2,
        points=4,
        action=no_op_action,
    ),
    WingspanBird(
        "Black Bellied whistling duck",
        habitat={Habitat.wetlands},
        foodcost=FoodCost([Food.seed, Food.seed], one_of=False),
        wingspan=76,
        nest_type=NestType.cavity,
        egg_capacity=5,
        points=2,
        action=no_op_action,
    ),
    WingspanBird(
        "Black Billed Magpie",
        habitat={Habitat.prairie, Habitat.wetlands},
        foodcost=FoodCost([Food.invertibrate], one_of=False),
        wingspan=64,
        nest_type=NestType.star,
        egg_capacity=3,
        points=3,
        action=no_op_action,
    ),
]
