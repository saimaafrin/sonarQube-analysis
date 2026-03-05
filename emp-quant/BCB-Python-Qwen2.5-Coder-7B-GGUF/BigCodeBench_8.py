
from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    # Convert elements in 'T1' to integers
    T1 = [int(x) for x in T1]
    
    # Calculate the total number of random integers to generate
    total_numbers = sum(T1)
    
    # Generate a list of random integers
    random_numbers = [randint(0, RANGE) for _ in range(total_numbers)]
    
    # Count the occurrences of each number in the generated list
    number_counts = Counter(random_numbers)
    
    # Output the Counter object
    return number_counts