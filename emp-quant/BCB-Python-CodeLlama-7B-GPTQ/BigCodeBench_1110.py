from collections import Counter
from operator import itemgetter
import itertools
def task_func(word_dict):
    """
    Given a dictionary of words as keys and letters as values, count the frequency of each letter in the words.
    The function should output with:
        dict: A dictionary with letters as keys and their frequencies as values.
    """
    # Create a list of all the letters in the words
    letters = [letter for word in word_dict for letter in word]

    # Create a Counter object to count the frequency of each letter
    counter = Counter(letters)

    # Create a dictionary with the letters as keys and their frequencies as values
    letter_freq = {letter: counter[letter] for letter in counter}

    return letter_freq
word_dict = {'cat': 'cac', 'dog': 'god'}