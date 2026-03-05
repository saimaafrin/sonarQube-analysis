
import collections
from queue import PriorityQueue
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    # Generate a random string of the given length
    random_string = ''.join(random.choice(LETTERS) for _ in range(string_length))

    # Count the frequency of each letter in the string
    letter_freq = collections.OrderedDict(
        (letter, random_string.count(letter)) for letter in LETTERS
    )

    # Sort the dictionary by frequency in descending order
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

    return collections.OrderedDict(sorted_freq)