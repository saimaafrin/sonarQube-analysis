
import collections
from queue import PriorityQueue
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    # Generate a random string of the given length
    random_string = ''.join(random.choice(LETTERS) for _ in range(string_length))
    
    # Count the frequency of each letter
    letter_frequency = collections.Counter(random_string)
    
    # Create a priority queue to sort letters by frequency in descending order
    pq = PriorityQueue()
    for letter, freq in letter_frequency.items():
        pq.put((-freq, letter))  # Negative frequency for max-heap behavior
    
    # Extract elements from the priority queue to get them in sorted order
    sorted_letter_frequency = collections.OrderedDict()
    while not pq.empty():
        freq, letter = pq.get()
        sorted_letter_frequency[letter] = -freq  # Convert back to positive frequency
    
    return sorted_letter_frequency