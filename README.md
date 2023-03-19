# Description

Wingspan the board game, implemented in Python. Designed for training AI agents.

# Helpful links

https://navarog.github.io/wingsearch/
https://wingsplain.com/wingspan-bird-card-tier-list/

## Board

3 x 5 grid of habitats:

## Rounds

4 rounds per game.
1st round - 8 turns
2nd round - 7 turns
3rd round - 6 turns
4th round - 5 turns

## End of round bonus

1. number of eggs in a given nest type
2. egg sets across habitats
3. number of birds in a given habitat
4. number of total birds
5. number of eggs on birds in a given habitat

## Representation

There are 4 possible initial actions each turn:

1. Play a bird card
   1. You must pay the cost of the bird card.
   2. Choose a habitat to place the bird card in.
   3. Trigger any special abilities of the bird card (if any).
2. Gain food
   1. Choose food from the bird feeder or reroll if available.
   2. Discard a card for an extra food (if applicable).
   3. Trigger bird card abilities in the forrest.
3. Lay eggs
   1. Discard a food for an extra egg (if applicable).
   2. Place eggs on available bird cards.
   3. Trigger bird card abilities in the Prairie.
4. Draw cards
   1. Draw card(s) from the deck.
   2. Discard an egg to draw an extra card.
   3. Trigger bird card abilities in the wetlands.

## Bird Cards

Each bird card consists of the following:

1. Name
2. Cost - 6 types (worm, seed, berry, fish, mouse, wild)
3. Habitat - 3 types (forrest, prairie, wetlands)
4. Points - can be 0 to 9
5. Nest type - 5 types (ground, bowl, cavity, platform, star)
6. Egg capacity - 0 to 7
7. Action - 3 main types (when played, between turns, activated)

## Food

1. Invertibrate
2. Seed
3. Fruit
4. Fish
5. Rodent
6. Invertibrate/seed

## Habitat

1. Forrest
2. Prairie
3. Wetlands

## Nest Types

1. Ground
2. Bowl
3. Cavity
4. Platform
5. Star

## Action Types

1. When Played
2. Between Turns
3. Activated

## Bonus Cards

Points based on the number of birds of various types.

# ML Representation

## Shared

- the 4 end of round goals. 1x4 matrix. Each goal is a number.
- Bird feeder. 1x6 matrix. 1-6 is a number representating food type. 6 is reroll possible yes/no.
- Number of dice outside of bird feeder (inferred from feeder)
- Face-up cards - 1x3
- Deck - [0 - 170]
- Bonus cards - [0 - 26]
- Discards - [0 - 170]

## Player

### Tucked/Cached

- points from tucked cards
- points from cached food

### Board representation

stack of 3x5 planes for each player.

- number of eggs in each square.
- bird card in each square.

### Bird cards in hand

Bird cards in hand.
1x20? matrix. integer for each bird card.

### Bonus cards in hand

Bonus cards in hand.
1x10? matrix. integer for each bonus card.

### Player food

1x5 matrix. Each location is the food type, integers of each food amount.

## Action representation

### Place bird card

3x5 matrix of 0s and 1s.

### Gain food

1x5 matrix of 0s and 1s.

### Lay eggs

3x5 matrix of 0s and 1s.

### Draw cards

1x3 matrix of 0s and 1s.

### Bird cards

- each bird is a number 0-170
- each bird card can be represented by a vector:
  - 0-5 (invertibrate,seed,...,wild) count of each food type required to play
  - 6 nest type
  - 7 nest capacity (number between 0-7)
  - 8 points
  - 9 wingspan
  - 10 action type (could be extraneous)
  - 11 action number (enum of actions)
