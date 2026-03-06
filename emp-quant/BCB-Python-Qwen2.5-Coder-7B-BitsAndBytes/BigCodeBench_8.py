
from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    # Convert elements in T1 to integers
    int_T1 = [int(x) for x in T1]
    
    # Calculate the total number of random integers to generate
    total_numbers = sum(int_T1)
    
    # Generate a list of random integers
    random_integers = [randint(0, RANGE) for _ in range(total_numbers)]
    
    # Count the occurrences of each number in the generated list
    counter = Counter(random_integers)
    
    return counter