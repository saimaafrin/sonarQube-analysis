
from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    # Convert elements in 'T1' to integers
    T1 = [int(x) for x in T1]
    
    # Calculate the sum of the integers in T1
    total_count = sum(T1)
    
    # Generate a list of random integers
    random_integers = [randint(0, RANGE) for _ in range(total_count)]
    
    # Count the occurrences of each number in the list
    counter = Counter(random_integers)
    
    # Output the Counter object
    return counter