
import collections
from queue import PriorityQueue
import random

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):
    # Generate a random string of the given length
    random_string = ''.join(random.choices(LETTERS, k=string_length))
    
    # Count the frequency of each letter
    frequency_counter = collections.Counter(random_string)
    
    # Create a priority queue to sort the letters by frequency in descending order
    priority_queue = PriorityQueue()
    for letter, frequency in frequency_counter.items():
        priority_queue.put((-frequency, letter))  # Negative frequency for max heap
    
    # Create an ordered dictionary from the priority queue
    ordered_dict = collections.OrderedDict()
    while not priority_queue.empty():
        frequency, letter = priority_queue.get()
        ordered_dict[letter] = -frequency  # Convert back to positive frequency
    
    return ordered_dict