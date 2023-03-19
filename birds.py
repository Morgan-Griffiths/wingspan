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
    start = 5

class ActionType(Enum):
    """ Enumerate all action types in the game Wingspan. """
    when_played = 1
    when_activated = 2
    once_between_turns = 3
    end_of_game = 4

class ActivatedType(Enum):
    hunter = 1
    flocking = 2
    none = 3

class Actions(Enum):
    player_a_second_bird_card_in_forest = 1
    player_a_second_bird_card_in_grassland = 1
    player_a_second_bird_card_in_wetlands = 1

    all_players_gain_one_seed = 1
    all_players_gain_one_berry = 1
    all_players_gain_one_worm = 1

    once_between_turns_if_forest_bird_gain_invertibrate = 1
    once_between_turns_if_lay_eggs_gain_egg_on_cup_nest = 1

    look_at_card_if_less_than_100_cm_tuck = 1
    look_at_card_if_less_than_75_cm_tuck = 1
    look_at_card_if_less_than_50_cm_tuck = 1

    gain_one_seed_from_supply_and_cache = 1
    gain_one_seed_from_birdfeeder_and_cache_if_you_want = 1

    discard_one_seed_tuck_two_cards = 1
    discard_one_egg_gain_one_wild_food = 1
    discard_one_egg_gain_two_wild_food = 1

    cache_one_food = 1
    draw_one_card = 1
    everyone_draws_one_card = 2
    draw_one_card_discard_one_card = 3
    tuck_one_card_from_hand_draw_one_card = 4
    tuck_one_card_from_hand_lay_one_egg = 4

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