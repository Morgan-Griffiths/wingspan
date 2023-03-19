from enum import Enum, auto

from wingspan.food import Food


class PlayerFood:
    def __init__(self):
        self.food = {
            Food.invertibrate: 0,
            Food.fish: 0,
            Food.fruit: 0,
            Food.rodent: 0,
            Food.seed: 0,
        }

    def add(self, food_type):
        self.food[Food[food_type]] += 1
