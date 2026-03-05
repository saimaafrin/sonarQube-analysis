import collections
from queue import PriorityQueue
import random
LETTERS = ['a', 'b', 'c', 'd', 'e']
def task_func(string_length=100):
    """
    Generate a random string of a given length from a predefined list of letters and count the frequency of each letter, returning an ordered dictionary sorted by frequency in descending order.
    """
    # Generate a random string
    random_string = ''.join(random.choice(LETTERS) for _ in range(string_length))

    # Count the frequency of each letter
    letter_freq = collections.Counter(random_string)

    # Sort the dictionary by frequency in descending order
    sorted_freq = collections.OrderedDict(sorted(letter_freq.items(), key=lambda t: t[1], reverse=True))

    return sorted_freq