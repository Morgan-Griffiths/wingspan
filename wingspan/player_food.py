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
        self.food[food_type] += 1

    def discard(self, food_type):
        self.food[food_type] -= 1

    def return_food_vector(self):
        return [self.food[Food.invertibrate], self.food[Food.fish], self.food[Food.fruit], self.food[Food.rodent], self.food[Food.seed]]

    def __repr__(self):
        return f'{self.food}'