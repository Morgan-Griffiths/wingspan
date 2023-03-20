import pickle
import numpy as np
import pandas as pd
import json


card_list_path = '/Users/Shuza/Code/Wingspan/wingspan-card-lists-20201118.xlsx'

df = pd.read_excel(card_list_path, sheet_name=1)
df = df.dropna(axis=1, how='all')
# drop the first 2 rows
df = df.drop([0, 1])

# iterate through the rows, zip column names with values

skip_cols = ['Scientific name', 'Unnamed: 2']
remaining_cols = [col for col in df.columns if col not in skip_cols]

nest_types = df['Nest type'].unique().tolist()
print(nest_types)
birds = []

power_categories = ['Caching Food', 'Egg-laying', 'Card-drawing', 'Flocking', 'Food from Supply', 'Hunting/Fishing', 'Food from Birdfeeder', 'Other']#df['PowerCategory'].dropna().unique().tolist()
print(power_categories)

for index, row in df.iterrows():
    bird = {}
    for col_name, col_value in zip(df.columns, row):
        if col_name in skip_cols:
            continue
        # if col_name == 
        if isinstance(col_value,str):
            col_value = col_value.lower()
            if col_value == 'x':
                col_value = True
        # check if value is nan
        elif pd.isna(col_value):
            col_value = False
        elif isinstance(col_value, float):
            col_value = int(col_value)
        col_name = col_name.replace(' ', '_')
        bird[col_name.lower()] = col_value
    birds.append(bird)
    
with open('birds.json', 'w') as f:
    f.write(json.dumps(birds))
# remaining_cols
# print(df.columns)

# print(df['PowerCategory'].unique())