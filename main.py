from wingspan.game import Game

if __name__ == "__main__":
    game = Game(1)
    game.reset()
    # game.play()
    print(len(game.deck))
