
from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    # Convert elements in T1 to integers
    T1_ints = [int(x) for x in T1]

    # Calculate the sum of the integers in T1
    sum_T1 = sum(T1_ints)

    # Generate a list of random integers with the same sum as T1
    random_ints = [randint(0, RANGE) for _ in range(sum_T1)]

    # Count the occurrences of each number in the generated list
    counter = Counter(random_ints)

    return counter