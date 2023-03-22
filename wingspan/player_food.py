from enum import Enum, auto
from wingspan.birds import WingspanBird
from wingspan.food import Food,food_name_dictionary
from wingspan.helpers import player_food_dictionary_stoi

import copy


class PlayerFood:
    def __init__(self):
        self.food = {
            Food.invertebrate: 0,
            Food.seed: 0,
            Food.fruit: 0,
            Food.rodent: 0,
            Food.fish: 0,
        }

    def add(self, food_type):
        self.food[food_type] += 1

    def discard(self, food_type):
        self.food[food_type] -= 1

    def return_food_vector(self):
        return [self.food[Food.invertebrate], self.food[Food.seed], self.food[Food.fruit], self.food[Food.rodent], self.food[Food.fish]]

    def __repr__(self):
        return f'{self.food}'
    
    def __contains__(self, bird_card:WingspanBird):
        print(bird_card)
        extra_food_cost = 0
        food_copy = copy.deepcopy(self.food)
        for food_type,amount in bird_card.food_cost.items():
            if food_type in ['invertebrate','seed','fruit','rodent','fish']:
                food_name = food_name_dictionary[food_type]
                if food_copy[food_name] >= amount:
                    food_copy[food_name] -= amount
                else:
                    extra_food_cost += (amount - food_copy[food_name]) * 2
                    food_copy[food_name] = 0
            elif food_type == 'wild':
                extra_food_cost += amount
        extra_food_cost -= sum(food_copy.values())
        return extra_food_cost <= 0