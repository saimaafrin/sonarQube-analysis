import random
from collections import Counter
from statistics import mode
def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    # Set the random seed if provided
    if random_seed is not None:
        random.seed(random_seed)
    
    # Generate a random list of integers within the specified range
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    
    # Find the mode of the list
    list_mode = mode(random_list)
    
    # Create a Counter object to count the frequency of each number in the list
    number_frequency = Counter(random_list)
    
    # Create a generator that yields tuples of each number and its frequency
    def number_generator():
        for number, frequency in number_frequency.items():
            yield (number, frequency)
    
    # Return the mode and the generator
    return list_mode, number_generator()