from collections import Counter
import itertools
from random import randint
def task_func(T1, RANGE=100):
    """
    Convert elements in 'T1' to integers and create a list of random integers where the number of integers is determined by the sum of the integers in 'T1'.
    Random integers are generated between 0 and 'RANGE' (default is 100).
    Count the occurrences of each number in the generated list using a Counter.
    """
    # Convert elements in 'T1' to integers
    T1_ints = [int(x) for x in T1]

    # Determine the number of random integers to generate
    num_ints = sum(T1_ints)

    # Generate a list of random integers
    random_ints = [randint(0, RANGE) for _ in range(num_ints)]

    # Count the occurrences of each number in the generated list
    counter = Counter(random_ints)

    return counter
T1 = ['a', 'b', 'c']