import pickle
import numpy as np
import pandas as pd
import json

from wingspan.bonus_deck import BonusNames


card_list_path = '/Users/Shuza/Code/Wingspan/wingspan-card-lists-20201118.xlsx'
# jq -r '[.[].power_text] | unique | .[]' birds.json | pbcopy

df = pd.read_excel(card_list_path, sheet_name=1)
df = df.dropna(axis=1, how='all')
# drop the first 2 rows
df = df.drop([0, 1])

# iterate through the rows, zip column names with values

skip_cols = ['scientific_name', 'unnamed:_2', 'total_food_cost']
food_cols = ['seed', 'fruit', 'fish', 'rodent', 'invertebrate','wild','/_(food_cost)']
action_cols = ['power_category','power_text','predator','flocking','draw_bonus_cards','action_type']
remaining_cols = [col for col in df.columns if col not in skip_cols]

birds = []
bonus_names = [x.lower() for x in filter(lambda x: x[0] != '_',dir(BonusNames))]

for index, row in df.iterrows():
    bird = {'bonuses': {},'habitat':{},'food_cost':{},'action':{}}
    for col_name, col_value in zip(df.columns, row):
        col_name = col_name.replace(' ', '_').lower()
        if col_name in skip_cols:
            continue
        if col_name == 'powercategory':
            col_name = 'power_category'
        elif col_name == 'common_name':
            col_name = 'name'
        elif col_name == 'wild_(food)':
            col_name = 'wild'
        elif col_name == 'bonus_card':
            col_name = 'draw_bonus_cards'
        elif col_name == 'victory_points':
            col_name = 'points'
        elif col_name == 'color':
            col_name = 'action_type'
        if isinstance(col_value,str):
            col_value = col_value.lower()
            if col_value == 'x':
                col_value = True
        # check if value is nan
        elif pd.isna(col_value):
            if col_name == 'powercategory':
                col_value = None
            elif col_name == '/_(food_cost)':
                col_value = False
            elif col_name in food_cols:
                col_value = 0
            else:
                col_value = False
        elif isinstance(col_value, float):
            col_value = int(col_value)
        if col_name in food_cols:
            bird['food_cost'][col_name] = col_value
        elif col_name in action_cols:
            bird['action'][col_name] = col_value
        elif col_name in ['forest','wetland','grassland']:
            bird['habitat'][col_name] = col_value
        elif col_name in bonus_names:
            bird['bonuses'][col_name] = col_value
        else:
            bird[col_name] = col_value
        
    birds.append(bird)
print(birds[0])
    
with open('birds.json', 'w') as f:
    json.dump(birds,f, default=lambda o: o.__dict__, indent=4)
# remaining_cols
# print(df.columns)

# print(df['PowerCategory'].unique())

""" 
bonus cards nested 
food nested
food false -> 0
habitat nested

powercategory false -> null
"""