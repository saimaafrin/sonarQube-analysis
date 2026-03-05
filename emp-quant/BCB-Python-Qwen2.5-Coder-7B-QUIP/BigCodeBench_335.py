
import collections
from queue import PriorityQueue
import random
# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    # Generate a random string of the given length
    random_string = ''.join(random.choices(LETTERS, k=string_length))
    
    # Count the frequency of each letter in the generated string
    letter_frequency = collections.Counter(random_string)
    
    # Sort the letters by their frequency in descending order
    sorted_letter_frequency = collections.OrderedDict(sorted(letter_frequency.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_letter_frequency