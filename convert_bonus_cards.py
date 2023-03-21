import pickle
import numpy as np
import pandas as pd
import json

from wingspan.bonus_deck import BonusCard

card_list_path = '/Users/Shuza/Code/Wingspan/wingspan-card-lists-20201118.xlsx'
# jq -r '[.[].power_text] | unique | .[]' birds.json | pbcopy

df = pd.read_excel(card_list_path, sheet_name=5)

bonus_cards = []
for index, row in df.iterrows():
    if row[1] != 'core':
        break
    if row[2] == 'X':
        row[2] = True
    elif pd.isna(row[2]):
        row[2] = False
    if pd.isna(row[4]):
        row[4] = ''
    bonus_cards.append(BonusCard(*row))

print(bonus_cards)

with open('bonus_cards.json', 'w') as f:
    json.dump(bonus_cards, f, default=lambda o: o.__dict__, indent=4)