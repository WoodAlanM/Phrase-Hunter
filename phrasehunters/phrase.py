# Create your Phrase class logic here.
from phrasehunters.character import Character


class Phrase:
    def __init__(self, phrase):
        letter_list = list(phrase)
        self.character_list = []
        for letter in letter_list:
            self.character_list.append(Character(letter))

    # This method checks the letter to each character object
    # if one is guessed it returns True
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

    # This method returns a list showing the appropriate character
    # from the phrase
    def return_letters(self):
        return_list = []
        for letters in self.character_list:
            return_list.append(letters.show_letter())
        return return_list

    # This method returns whether or not the entire word has been uncovered
    def guessed_entire_word(self):
        whole_word = False
        a_list = []
        for letter in self.character_list:
            a_list.append(letter.show_letter())
        return "_" not in a_list

