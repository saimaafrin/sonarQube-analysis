
from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    # Convert T1 to a list of integers
    T1_ints = [int(x) for x in T1]

    # Calculate the sum of the integers in T1
    sum_of_ints = sum(T1_ints)

    # Generate a list of random integers
    random_ints = [randint(0, RANGE) for _ in range(sum_of_ints)]

    # Count the occurrences of each number in the generated list
    counter = Counter(random_ints)

    return counter