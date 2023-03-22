
from enum import Enum, auto
from itertools import count

from wingspan.food import Food

                                      
class GameActions(Enum):
    forest_one = auto()
    forest_two = auto()
    forest_three = auto()
    forest_four = auto()
    forest_five = auto()
    prairie_one = auto()
    prairie_two = auto()
    prairie_three = auto()
    prairie_four = auto()
    prairie_five = auto()
    wetlands_one = auto()
    wetlands_two = auto()
    wetlands_three = auto()
    wetlands_four = auto()
    wetlands_five = auto()
    bird_feeder_one = auto()
    bird_feeder_two = auto()
    bird_feeder_three = auto()
    bird_feeder_four = auto()
    bird_feeder_five = auto()
    bird_feeder_reroll = auto()
    invertebrate = auto()
    seed = auto()
    fruit = auto()
    rodent = auto()
    fish = auto()
    player_hand_one = auto()
    player_hand_two = auto()
    player_hand_three = auto()
    player_hand_four = auto()
    player_hand_five = auto()
    player_hand_six = auto()
    player_hand_seven = auto()
    player_hand_eight = auto()
    player_hand_nine = auto()
    player_hand_ten = auto()
    player_hand_eleven = auto()
    player_hand_twelve = auto()
    player_hand_thirteen = auto()
    player_hand_fourteen = auto()
    player_hand_fifteen = auto()
    player_hand_sixteen = auto()
    player_hand_seventeen = auto()
    player_hand_eighteen = auto()
    player_hand_nineteen = auto()
    player_hand_twenty = auto()
    player_bonus_card_one = auto()
    player_bonus_card_two = auto()
    player_bonus_card_three = auto()
    player_bonus_card_four = auto()
    player_bonus_card_five = auto()
    player_bonus_card_six = auto()
    player_bonus_card_seven = auto()
    player_bonus_card_eight = auto()
    draw_from_deck = auto()
    draw_from_faceup_one = auto()
    draw_from_faceup_two = auto()
    draw_from_faceup_three = auto()
    play_a_bird_card = auto()
    gain_food = auto()
    lay_eggs = auto()
    draw_cards = auto()
    activate_bird_card = auto()
    no_op = auto()
    choose_player_one = auto()
    choose_player_two = auto()
    choose_player_three = auto()

    def get_value(self):
        return self.value - 1

# GameActions = Enum('GameActions',
#                    zip(['forest one','forest two','forest three','forest four','forest five',
#                         'prairie one','prairie two','prairie three','prairie four','prairie five',
#                         'wetlands one','wetlands two','wetlands three','wetlands four','wetlands five',
#                         'bird feeder one','bird feeder two','bird feeder three','bird feeder four','bird feeder five','bird feeder reroll',
#                         'one','two','three','four','five',
#                         'player hand one','player hand two','player hand three','player hand four','player hand five','player hand six','player hand seven','player hand eight','player hand nine','player hand ten','player hand eleven','player hand twelve','player hand thirteen','player hand fourteen','player hand fifteen','player hand sixteen','player hand seventeen','player hand eighteen','player hand nineteen','player hand twenty',
#                         'player bonus card one','player bonus card two','player bonus card three','player bonus card four','player bonus card five','player bonus card six','player bonus card seven','player bonus card eight',
#                         'draw from deck','draw from faceup one','draw from faceup two','draw from faceup three',
#                         'play a bird card','gain food','lay eggs','draw cards',
#                         'activate bird card','no op',
#                         'choose player one','choose player two','choose player three'],count()))

player_hand_dictionary_itos = {
    0: 'player hand one',
    1: 'player hand two',
    2: 'player hand three',
    3: 'player hand four',
    4: 'player hand five',
}
player_hand_dictionary_stoi = {v: k for k, v in player_hand_dictionary_itos.items()}

player_food_dictionary_itos = {
    0: 'invertebrate',
    1: 'seed',
    2: 'fruit',
    3: 'rodent',
    4: 'fish',
}
player_food_dictionary_stoi = {v: k for k, v in player_food_dictionary_itos.items()}

player_bonus_card_dictionary_itos = {
    0: 'player bonus card one',
    1: 'player bonus card two',
    2: 'player bonus card three',
    3: 'player bonus card four',
    4: 'player bonus card five',
    5: 'player bonus card six',
    6: 'player bonus card seven',
    7: 'player bonus card eight',
}
player_bonus_card_dictionary_stoi = {v: k for k, v in player_bonus_card_dictionary_itos.items()}

action_dictionary = {
    0: 'forest one',
    1: 'forest two',
    2: 'forest three',
    3: 'forest four',
    4: 'forest five',
    5: 'prairie one',
    6: 'prairie two',
    7: 'prairie three',
    8: 'prairie four',
    9: 'prairie five',
    10: 'wetlands one',
    11: 'wetlands two',
    12: 'wetlands three',
    13: 'wetlands four',
    14: 'wetlands five',
    15: 'bird feeder one',
    16: 'bird feeder two',
    17: 'bird feeder three',
    18: 'bird feeder four',
    19: 'bird feeder five',
    20: 'bird feeder reroll',
    21: Food.invertebrate,
    22: Food.seed,
    23: Food.fruit,
    24: Food.rodent,
    25: Food.fish,
    26: 'player hand one',
    27: 'player hand two',
    28: 'player hand three',
    29: 'player hand four',
    30: 'player hand five',
    31: 'player hand six',
    32: 'player hand seven',
    33: 'player hand eight',
    34: 'player hand nine',
    35: 'player hand ten',
    36: 'player hand eleven',
    37: 'player hand twelve',
    38: 'player hand thirteen',
    39: 'player hand fourteen',
    40: 'player hand fifteen',
    41: 'player hand sixteen',
    42: 'player hand seventeen',
    43: 'player hand eighteen',
    44: 'player hand nineteen',
    45: 'player hand twenty',
    46: 'player bonus card one',
    47: 'player bonus card two',
    48: 'player bonus card three',
    49: 'player bonus card four',
    50: 'player bonus card five',
    51: 'player bonus card six',
    52: 'player bonus card seven',
    53: 'player bonus card eight',
    54: 'draw from deck',
    55: 'draw from faceup one',
    56: 'draw from faceup two',
    57: 'draw from faceup three',
    58: 'play a bird',
    59: 'gain food',
    60: 'lay eggs',
    61: 'draw cards',
    62: 'activate bird card',
    63: 'no op',
    64: 'choose player one',
    65: 'choose player two',
    66: 'choose player three',
}

human_readable_action_dictionary = {v:k for k,v in action_dictionary.items()}
class UIState(Enum):
    initial_discard_cards = auto()
    initial_discard_food = auto()
    initial_discard_bonus_cards = auto()
    round_1 = auto()
    round_2 = auto()
    round_3 = auto()
    round_4 = auto()
    game_over = auto()

    def __repr__(self) -> str:
        return self.name
    
class IntermediateState(Enum):
    no_op = auto()
    picking_bird_card_in_hand =  auto()
    picking_player_food = auto()
    picking_feeder_food = auto()
    picking_bonus_card_to_keep = auto()
    choosing_habitat_to_play_bird = auto()
    choosing_bird_on_board = auto()
    choosing_player = auto()
    laying_eggs_on_bird = auto()
    discarding_or_tucking_card_from_hand = auto()
    picking_card_to_draw = auto()
    

class Habitat(Enum):
    forest = auto()
    prairie = auto()
    wetlands = auto()

class PowerCategories(Enum):
    caching_food = auto()
    egg_laying = auto()
    card_drawing = auto()
    flocking = auto()
    food_from_supply = auto()
    hunting_fishing = auto()
    food_from_birdfeeder = auto()
    other = auto()

class PowerColors(Enum):
    brown = auto()
    pink = auto()
    white = auto()


habitat_dict = {
    'forest': Habitat.forest.value - 1,
    'prairie': Habitat.prairie.value - 1,
    'wetlands': Habitat.wetlands.value - 1,
}


