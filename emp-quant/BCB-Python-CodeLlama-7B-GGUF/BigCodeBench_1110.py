
from collections import Counter
from operator import itemgetter
import itertools

def task_func(word_dict):
    # Create a list of all the letters in the words
    all_letters = [letter for word in word_dict for letter in word]

    # Create a Counter object with the letters as keys and their frequencies as values
    letter_counter = Counter(all_letters)

    # Sort the Counter object by frequency
    sorted_counter = sorted(letter_counter.items(), key=itemgetter(1), reverse=True)

    # Return the sorted Counter object
    return sorted_counter