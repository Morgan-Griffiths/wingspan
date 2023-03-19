import random

class Feeder:
    def __init__(self):
        self.feeder = [],
        self.picked = [],

    def roll(self):
        self.feeder = [random.randint(1, 7) for _ in range(5)]

    def pick(self, index):
        self.picked.append(self.feeder.pop(index))
    
    def reset(self):
        self.picked = []
        self.roll()

    def render(self):
        print("feeder")
        print("feeder: ", self.feeder)
        print("picked: ", self.picked)