import random
from collections import Counter
from statistics import mode
def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    
    # Generate a random list of integers within the specified range
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    
    # Find the mode of the list
    list_mode = mode(random_list)
    
    # Convert the list to a generator object that yields tuples (number, frequency)
    number_frequency_generator = ((num, random_list.count(num)) for num in set(random_list))
    
    return list_mode, number_frequency_generator