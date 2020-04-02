# Create your Character class logic in here.


class Character:
    def __init__(self, char, was_guessed=False):
        self.char = char
        self.was_guessed = was_guessed

    def change_guess(self):
        self.was_guessed = True

    def guess(self, guess_letter):
        if self.char.upper() == guess_letter.upper():
            self.change_guess()
            return True
        else:
            return False

    def show_letter(self):
        value = "_"
        if self.was_guessed:
            return self.char
        else:
            return value

