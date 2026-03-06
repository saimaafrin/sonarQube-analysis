
from collections import Counter
from operator import itemgetter
import itertools

def task_func(word_dict):
    # Create a Counter object to store the letter frequencies
    letter_freq = Counter()

    # Iterate over the words in the dictionary
    for word in word_dict:
        # Iterate over the letters in the word
        for letter in word:
            # Increment the frequency of the letter in the Counter object
            letter_freq[letter] += 1

    # Sort the Counter object by frequency and return it
    return sorted(letter_freq.items(), key=itemgetter(1), reverse=True)