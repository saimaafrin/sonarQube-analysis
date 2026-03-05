
import collections
from queue import PriorityQueue
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    """
    Generate a random string of a given length from a predefined list of letters
    and count the frequency of each letter, returning an ordered dictionary sorted
    by frequency in descending order.
    """
    # Generate a random string of the given length
    random_string = ''.join(random.choice(LETTERS) for _ in range(string_length))

    # Count the frequency of each letter in the string
    letter_freq = collections.Counter(random_string)

    # Sort the dictionary by frequency in descending order
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

    # Return an ordered dictionary sorted by frequency
    return collections.OrderedDict(sorted_freq)