from enum import Enum, auto

from wingspan.food import Food


class ActionType(Enum):
    """Enumerate all action types in the game Wingspan."""

    when_played = 1
    when_activated = 2
    once_between_turns = 3
    end_of_game = 4


class Actions(Enum):
    play_a_second_bird_card_in_forest = auto()
    play_a_second_bird_card_in_grassland = auto()
    play_a_second_bird_card_in_wetlands = auto()

    all_players_gain_one_seed = auto()
    all_players_gain_one_fruit = auto()
    all_players_gain_one_invertebrate = auto()
    all_players_gain_one_rodent = auto()
    all_players_gain_one_fish = auto()

    all_players_gain_one_egg_on_cavity_lay_additional_egg = auto()

    roll_dice_not_in_birdfeeder_gain_rodents_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_fish_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_fruit_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_invertebrate_if_available = auto()
    roll_dice_not_in_birdfeeder_gain_seed_if_available = auto()

    lay_egg_on_bird = auto()
    lay_egg_on_any_bird = auto()

    draw_one_cards = auto()
    draw_two_cards = auto()
    draw_two_bonus_cards_discard_one = auto()

    pick_a_player_to_pick_food_from_bird_feeder = auto()

    once_between_turns_if_forest_bird_played_gain_one_invertebrate = auto()
    once_between_turns_if_wetland_bird_played_gain_one_fish = auto()
    once_between_turns_if_lay_eggs_gain_egg_on_cup_nest = auto()
    once_between_turns_if_gainfood_gain_one_rodent = auto()

    look_at_card_if_less_than_100_cm_tuck = auto()
    look_at_card_if_less_than_75_cm_tuck = auto()
    look_at_card_if_less_than_50_cm_tuck = auto()

    # Gain
    gain_one_invertebrate = auto()
    gain_one_seed = auto()
    gain_one_fruit = auto()
    gain_one_fish = auto()
    gain_one_rodent = auto()

    gain_one_invertebrate_from_birdfeeder = auto()
    gain_one_seed_from_birdfeeder = auto()
    gain_one_fruit_from_birdfeeder = auto()
    gain_one_fish_from_birdfeeder = auto()
    gain_one_rodent_from_birdfeeder = auto()

    gain_three_invertebrate_from_supply = auto()
    gain_three_seed_from_supply = auto()
    gain_three_fruit_from_supply = auto()
    gain_three_rodent_from_supply = auto()
    gain_three_fish_from_supply = auto()

    gain_all_invertebrate_from_birdfeeder = auto()
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


def no_op():
    ...


def all_gain_food(game, food_type):
    for player in game.players:
        player.food.add(food_type)


def initial_discards(game, player):
    player_choices = player.hand
    # get all possible discards
    # ask player what they want to discard or continue
    input()  # for ai, we replace with query model (playernum)
    # repeat if not continue


# jq -r '[.[].power_text] | unique | .[]' birds.json | pbcopy
actions = {
    "all players draw 1 [card] from the deck.": no_op,
    "all players gain 1 [fish] from the supply.": lambda game: all_gain_food(
        game, Food.fish
    ),
    "all players gain 1 [fruit] from the supply.": lambda game: all_gain_food(
        game, Food.fruit
    ),
    "all players gain 1 [invertebrate] from the supply.": lambda game: all_gain_food(
        game, Food.invertebrate
    ),
    "all players gain 1 [seed] from the supply.": lambda game: all_gain_food(
        game, Food.seed
    ),
    "all players gain a [fruit] from the supply.": lambda game: all_gain_food(
        game, Food.fruit
    ),
    "all players lay 1 [egg] on any 1 [bowl] bird. you may lay 1 [egg] on 1 additional [bowl] bird.": no_op,
    "all players lay 1 [egg] on any 1 [cavity] bird. you may lay 1 [egg] on 1 additional [cavity] bird.": no_op,
    "all players lay 1 [egg] on any 1 [ground] bird. you may lay 1 [egg] on 1 additional [ground] bird.": no_op,
    "discard 1 [egg] from any of your other birds to gain 1 [wild] from the supply.": no_op,
    "discard 1 [egg] from any of your other birds to gain 2 [wild] from the supply.": no_op,
    "discard 1 [egg] to draw 2 [card].": no_op,
    "discard 1 [seed] to tuck 2 [card] from the deck behind this bird.": no_op,
    "discard [fish] to tuck 2 [card] from the deck behind this bird.": no_op,
    "discard a [fish] to tuck 2 [card] from the deck behind this bird.": no_op,
    "draw 1 [card].": no_op,
    "draw 1 [card]. if you do, discard 1 [card] from your hand at the end of your turn.": no_op,
    "draw 2 [card].": no_op,
    "draw 2 [card]. if you do, discard 1 [card] from your hand at the end of your turn.": no_op,
    "draw 2 new bonus cards and keep 1.": no_op,
    "draw [card] equal to the number of players +1. starting with you and proceeding clockwise, each player selects 1 of those cards and places it in their hand. you keep the extra card.": no_op,
    "draw the 3 face-up [card] in the bird tray.": no_op,
    "each player gains 1 [die] from the birdfeeder, starting with the player of your choice.": no_op,
    "gain 1 [fruit] from the supply.": no_op,
    "gain 1 [invertebrate] from the birdfeeder, if there is one.": no_op,
    "gain 1 [invertebrate] from the supply.": no_op,
    "gain 1 [invertebrate] or [fruit] from the birdfeeder, if there is one.": no_op,
    "gain 1 [seed] from the birdfeeder (if available). you may cache it on this card.": no_op,
    "gain 1 [seed] from the supply and cache it on this card.": no_op,
    "gain 1 [seed] from the supply.": no_op,
    "gain 1 [seed] or [fruit] from the birdfeeder, if there is one.": no_op,
    "gain 1 [wild] from the birdfeeder.": no_op,
    "gain 3 [fish] from the supply.": no_op,
    "gain 3 [seed] from the supply.": no_op,
    "gain all [fish] that are in the birdfeeder.": no_op,
    "gain all [invertebrate] that are in the birdfeeder.": no_op,
    "if this bird is to the right of all other birds in its habitat, move it to another habitat.": no_op,
    "lay 1 [egg] on any bird.": no_op,
    "lay 1 [egg] on each of your birds with a [bowl] nest.": no_op,
    "lay 1 [egg] on each of your birds with a [cavity] nest.": no_op,
    "lay 1 [egg] on each of your birds with a [ground] nest.": no_op,
    "lay 1 [egg] on each of your birds with a [platform] nest.": no_op,
    "lay 1 [egg] on this bird.": no_op,
    "look at a [card] from the deck. if <100cm, tuck it behind this bird. if not, discard it.": no_op,
    "look at a [card] from the deck. if <50cm, tuck it behind this bird. if not, discard it.": no_op,
    "look at a [card] from the deck. if <75cm, tuck it behind this bird. if not, discard it.": no_op,
    "play a second bird in your [forest]. pay its normal cost.": no_op,
    "play a second bird in your [grassland] or [forest]. pay its normal cost.": no_op,
    "play a second bird in your [grassland]. pay its normal cost.": no_op,
    "play a second bird in your [wetland]. pay its normal cost.": no_op,
    "player(s) with fewest [forest] birds gain 1 [die] from birdfeeder.": no_op,
    "player(s) with the fewest [wetland] birds: draw 1 [card].": no_op,
    "repeat 1 [predator] power in this habitat.": no_op,
    "repeat a brown power on one other bird in this habitat.": no_op,
    "roll all dice not in birdfeeder. if any are [fish], gain 1 [fish] and cache it on this card.": no_op,
    "roll all dice not in birdfeeder. if any are [rodent], gain 1 [rodent] and cache it on this card.": no_op,
    "roll all dice not in birdfeeder. if any are a [rodent], gain 1 [rodent] and cache it on this card.": no_op,
    "trade 1 [wild] for any other [wild] from the supply.": no_op,
    "tuck a [card] from your hand behind this bird. if you do, also lay 1 [egg] on this bird.": no_op,
    "tuck a [card] from your hand behind this bird. if you do, draw 1 [card].": no_op,
    "tuck a [card] from your hand behind this bird. if you do, gain 1 [fruit] from the supply.": no_op,
    "tuck a [card] from your hand behind this bird. if you do, gain 1 [invertebrate] from the supply.": no_op,
    "tuck a [card] from your hand behind this bird. if you do, gain 1 [invertebrate] or 1 [seed] from the supply.": no_op,
    "tuck a [card] from your hand behind this bird. if you do, gain 1 [seed] from the supply.": no_op,
    "tuck a [card] from your hand behind this bird. if you do, lay 1 [egg] on any bird.": no_op,
    "when another player plays a [forest] bird, gain 1 [invertebrate] from the supply.": no_op,
    "when another player plays a [grassland] bird, tuck 1 [card] from your hand behind this bird.": no_op,
    "when another player plays a [wetland] bird, gain 1 [fish] from the supply.": no_op,
    'when another player takes the "gain food" action, if they gain any number of [rodent], also gain 1 [rodent] from the supply and cache it on this card.': no_op,
    'when another player takes the "lay eggs" action, this bird lays 1 [egg] on another bird with a [bowl] nest.': no_op,
    'when another player takes the "lay eggs" action, this bird lays 1 [egg] on another bird with a [cavity] nest.': no_op,
    'when another player takes the "lay eggs" action, this bird lays 1 [egg] on another bird with a [ground] nest.': no_op,
    "when another player's predator succeeds, gain 1 [die] from the birdfeeder.": no_op,
}
