import collections
from queue import PriorityQueue
import random
LETTERS = ['a', 'b', 'c', 'd', 'e']
def task_func(string_length=100):
    # Generate a random string of the given length
    random_string = ''.join(random.choice(LETTERS) for _ in range(string_length))
    
    # Count the frequency of each letter
    letter_frequency = collections.Counter(random_string)
    
    # Create a priority queue to sort letters by frequency in descending order
    priority_queue = PriorityQueue()
    for letter, frequency in letter_frequency.items():
        priority_queue.put((-frequency, letter))  # Negative frequency for max heap
    
    # Create an ordered dictionary to store sorted letters and their frequencies
    sorted_frequency = collections.OrderedDict()
    while not priority_queue.empty():
        frequency, letter = priority_queue.get()
        sorted_frequency[letter] = -frequency  # Convert back to positive frequency
    
    return sorted_frequency