from wingspan.game import Game
import pickle

if __name__ == "__main__":
    game = Game(1)
    observation, reward, done = game.reset()
    while not done:
        print(f"Current state {observation}")
        action = input("Action: ")
        observation, reward, done = game.step(action)
    game.play()
