from random import shuffle

class Goal:
    def __init__(self,name):
        self.name = name

goal_list = [
    Goal("Eggs in Prairie"),
    Goal("Eggs in Wetlands"),
    Goal("Eggs in Forest"),
    Goal("Birds in Forest"),
    Goal("Birds in Wetlands"),
    Goal("Birds in Prairie"),
    Goal("Sets of eggs in all 3 habitats"),
    Goal("Total birds"),
    Goal("Eggs in cavity nests"),
    Goal("Eggs in bowl nests"),
    Goal("Eggs in ground nests"),
    Goal("Eggs in platform nests"),
]

class Goals:
    def __init__(self):
        self.reset()

    def reset(self):
        self.goals = goal_list.copy()
        shuffle(self.goals)
        self.current_goals = []

    def draw(self,n=4):
        for _ in range(n):
            self.current_goals.append(self.goals.pop())

    def render(self):
        print("goals")
        for goal in self.goals:
            print(goal.name)