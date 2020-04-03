# Import your Game class

from phrasehunters.game import Game

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop

phrase_list = [
    "Time is money",
    "Show me the money",
    "Hello world"
]


def main():
    a_game = Game(phrase_list)
    a_game.start_game()


if __name__ == "__main__":
    main()