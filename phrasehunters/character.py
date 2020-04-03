# Create your Character class logic in here.


class Character:
    def __init__(self, char, was_guessed=False):
        self.char = char
        self.was_guessed = was_guessed

    # Changes whether or not the character has been guessed
    def change_guess(self):
        self.was_guessed = True

    # Runs a guess against the character
    def guess(self, guess_letter):
        if self.char.upper() == guess_letter.upper():
            self.change_guess()
            return True
        else:
            return False
    # Returns an underscore if the letter has not been guessed
    # otherwise it returns the letter
    def show_letter(self):
        if self.was_guessed:
            return self.char
        elif self.char == " ":
            return " "
        else:
            return "_"

