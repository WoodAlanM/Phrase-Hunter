# Create your Game class logic in here.
import random

from phrasehunters.phrase import Phrase


class Game:
    def __init__(self, phrases):
        self.guessed_list = []
        self.phrases = phrases
        self.current_phrase = []
        phrase_number = random.randint(0, len(self.phrases) - 1)
        self.current_phrase = self.phrases[phrase_number]
        self.phrase_inst = Phrase(self.current_phrase)

    # Method for showing the letters
    def show_letters(self):
        letters_list = self.phrase_inst.return_letters()
        letters_string = " ".join(letters_list)
        print(letters_string)

    def guess(self, letter):
        if str(letter) in self.guessed_list:
            return True
        else:
            self.guessed_list.append(str(letter))
            return False

    # Start game
    def start_game(self):
        game_going = True
        lives = 5

        # User welcome
        print("--------------------------")
        print("Welcome to Phrase Hunter!!")
        print("--------------------------")
        print("\n")
        print("Lives left: {}".format(str(lives)))
        print("\n")
        print("Here is your word:")
        print("\n")
        self.show_letters()
        # Loop for user interaction
        while game_going:
            try:
                letter = input("Please enter a letter: ")
            except:
                print("Please only enter a letter.")
                continue
            if len(letter) != 1:
                print("Please enter only one letter.")
                continue
            elif not letter.isalpha():
                print("Please only enter a letter.")
                continue
            elif self.guess(letter):
                print("Please choose a letter you have not chosen already.")
                continue
            else:
                print("Thanks, checking letter...\n")
            guess = self.phrase_inst.check_guess(letter)
            if guess:
                if self.phrase_inst.guessed_entire_word():
                    print("\n")
                    print("You did it!!  You had {} lives left.".format(str(lives)))
                    print("Thanks for playing!!")
                    break
                else:
                    print("Good job! You have {} lives left.".format(str(lives)))
                    print("\n")
                    self.show_letters()
                    continue
            else:
                if lives == 1:
                    print("Im sorry, that was your last attempt. Goodbye.")
                    break
                else:
                    lives -= 1
                    print("That guess was incorrect.  Please try again.\n")
                    print("\n")
                    print("Lives left: {}".format(str(lives)))
                    print("\n")
            self.show_letters()
            print("\n")