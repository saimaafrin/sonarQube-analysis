
import random
import bisect
from array import array

def task_func(n=10, total=100):
    # Generate 'n' random integers
    numbers = [random.randint(1, total) for _ in range(n)]

    # Sort the numbers
    numbers.sort()

    # Determine the insertion position for a new number
    insertion_position = bisect.bisect_left(numbers, total - sum(numbers))

    # Return the sorted numbers and the insertion position
    return (array('i', numbers), insertion_position)