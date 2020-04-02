# Create your Phrase class logic here.
from phrasehunters.character import Character


class Phrase:
    def __init__(self, phrase):
        letter_list = list(phrase)
        self.character_list = []
        for letter in letter_list:
            self.character_list.append(Character(letter))

    def check_guess(self, letter):
        one_guessed = False
        is_guessed = False
        for character in self.character_list:
            one_guessed = character.guess(letter)
            if one_guessed:
                is_guessed = True
            else:
                continue
        return is_guessed

    def return_letters(self):
        return_list = []
        for letters in self.character_list:
            return_list.append(letters.show_letter())
        return return_list

    def guessed_entire_word(self):
        whole_word = False
        a_list = []
        for letter in self.character_list:
            a_list.append(letter.show_letter())
        return "_" not in a_list

