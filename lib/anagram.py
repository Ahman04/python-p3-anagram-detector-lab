# your code goes here!
 
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)

        # Return only words that have the same sorted letters
        matches = [
            w for w in word_list
            if sorted(w.lower()) == sorted_word
        ]

        return matches
