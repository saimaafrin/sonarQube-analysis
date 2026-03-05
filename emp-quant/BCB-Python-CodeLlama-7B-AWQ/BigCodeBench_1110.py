from collections import Counter
from operator import itemgetter
import itertools
def task_func(word_dict):
    """
    Given a dictionary of words as keys and letters as values, count the frequency of each letter in the words.
    The function should output with:
        dict: A dictionary with letters as keys and their frequencies as values.
    """
    # Create a dictionary to store the letter frequencies
    letter_freq = {}

    # Iterate over the words in the dictionary
    for word in word_dict:
        # Get the letters in the word
        letters = word.split()

        # Iterate over the letters in the word
        for letter in letters:
            # Increment the frequency of the letter
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    # Return the letter frequencies
    return letter_freq
word_dict = {'apple': 'a', 'banana': 'b', 'cherry': 'c'}