from wingspan.game import Game

def get_player_input(valid_actions):
    print(f'Valid actions {valid_actions}')
    action = input("Action: ")
    while True:
        try:
            valid_actions[int(action)]
            break
        except Exception as e:
            print("Invalid action")
            action = input("Action: ")
    return valid_actions[int(action)]

if __name__ == "__main__":
    game = Game(1)
    observation,valid_actions,done = game.reset()
    while not done:
        print(f'Current state {observation}')
        action = get_player_input(valid_actions)
        observation,valid_actions,done = game.step(action)
    game.play()
