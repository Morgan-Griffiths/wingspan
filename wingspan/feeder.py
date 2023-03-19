import random

class Feeder:
    def __init__(self):
        self.feeder = [],
        self.used_dice = [],

    def roll(self):
        self.feeder = [random.randint(1, 7) for _ in range(5)]

    def roll_used_dice(self):
        self.used_dice = [random.randint(1, 7) for _ in range(len(self.used_dice))]

    def pick(self, index):
        self.used_dice.append(self.feeder.pop(index))
    
    def reset(self):
        self.used_dice = []
        self.roll()

    def render(self):
        print("feeder")
        print("feeder: ", self.feeder)
        print("used_dice: ", self.used_dice)