
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

    # Create a generator that yields tuples of numbers and their frequencies
    number_frequency = Counter(random_list)
    number_generator = ((num, freq) for num, freq in number_frequency.items())

    return list_mode, number_generator