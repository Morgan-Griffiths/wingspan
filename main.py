from wingspan.game import Game
import pickle

if __name__ == "__main__":
    game = Game(1)
    observation,valid_actions,reward,done = game.reset()
    while not done:
        print(f'Current state {observation}')
        print(f'Valid actions {valid_actions}')
        action = input("Action: ")
        print(action)
        observation,valid_actions,reward,done = game.step(int(action))
    game.play()
