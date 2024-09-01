# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Store the word in lowercase for case insensitivity

    def match(self, possible_anagrams):
        # Prepare the sorted version of the original word
        sorted_word = ''.join(sorted(self.word))
        
        # Initialize a list to collect matches
        matches = []
        
        # Iterate through possible anagrams
        for candidate in possible_anagrams:
            # Check if the candidate is an anagram
            if ''.join(sorted(candidate.lower())) == sorted_word:
                matches.append(candidate)
        
        return matches
