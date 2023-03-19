
from enum import Enum, auto

class ActionType(Enum):
    """ Enumerate all action types in the game Wingspan. """
    when_played = 1
    when_activated = 2
    once_between_turns = 3
    end_of_game = 4

class Actions(Enum):
    player_a_second_bird_card_in_forest = auto()
    player_a_second_bird_card_in_grassland = auto()
    player_a_second_bird_card_in_wetlands = auto()

    all_players_gain_one_seed = auto()
    all_players_gain_one_fruit = auto()
    all_players_gain_one_invertibrate = auto()
    all_players_gain_one_rodent = auto()
    all_players_gain_one_fish = auto()

    all_players_gain_one_egg_on_cavity_lay_additional_egg = auto()

    roll_dice_not_in_birdfeeder_gain_rodents_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_fish_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_fruit_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_invertibrate_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_seed_if_available = auto()

    lay_egg_on_bird = auto()
    lay_egg_on_any_bird = auto()

    draw_one_cards = auto()
    draw_two_cards = auto()
    draw_two_bonus_cards_discard_one = auto()

    pick_a_player_to_pick_food_from_bird_feeder = auto()

    once_between_turns_if_forest_bird_played_gain_one_invertibrate = auto()
    once_between_turns_if_wetland_bird_played_gain_one_fish = auto()
    once_between_turns_if_lay_eggs_gain_egg_on_cup_nest = auto()
    once_between_turns_if_gainfood_gain_one_rodent = auto()

    look_at_card_if_less_than_100_cm_tuck = auto()
    look_at_card_if_less_than_75_cm_tuck = auto()
    look_at_card_if_less_than_50_cm_tuck = auto()

    # Gain
    gain_one_invertibrate = auto()
    gain_one_seed = auto()
    gain_one_fruit = auto()
    gain_one_fish = auto()
    gain_one_rodent = auto()

    gain_one_invertibrate_from_birdfeeder = auto()
    gain_one_seed_from_birdfeeder = auto()
    gain_one_fruit_from_birdfeeder = auto()
    gain_one_fish_from_birdfeeder = auto()
    gain_one_rodent_from_birdfeeder = auto()

    gain_three_invertibrate_from_supply = auto()
    gain_three_seed_from_supply = auto()
    gain_three_fruit_from_supply = auto()
    gain_three_rodent_from_supply = auto()
    gain_three_fish_from_supply = auto()

    gain_all_invertibrate_from_birdfeeder = auto()
    gain_all_seed_from_birdfeeder = auto()
    gain_all_fruit_from_birdfeeder = auto()
    gain_all_fish_from_birdfeeder = auto()
    gain_all_rodent_from_birdfeeder = auto()
    gain_one_seed_from_supply_and_cache = auto()
    gain_one_seed_from_birdfeeder_and_cache_if_you_want = auto()

    players_with_fewest_birds_in_forest_gain_one_food_from_birdfeeder = auto()
    players_with_fewest_birds_in_prairie_gain_one_food_from_birdfeeder = auto()
    players_with_fewest_birds_in_wetlands_gain_one_food_from_birdfeeder = auto()

    when_another_player_hunter_succeeds_gain_rodent = auto()
    when_another_player_hunter_succeeds_gain_fish = auto()

    repeat_one_bird_action = auto()
    repeat_one_hunter_action = auto()

    trade_one_food_for_wild_food = auto()

    discard_one_seed_tuck_two_cards = auto()
    discard_one_fish_tuck_two_cards = auto()
    discard_one_egg_gain_one_wild_food = auto()
    discard_one_egg_gain_two_wild_food = auto()
    discard_one_egg_gain_one_cards = auto()
    discard_one_egg_gain_two_cards = auto()

    cache_one_food = auto()
    all_players_draw_one_card = auto()
    draw_one_card_discard_one_card = auto()
    tuck_one_card_from_hand_draw_one_card = auto()
    tuck_one_card_from_hand_lay_one_egg_on_this_bird = auto()