import random
import bisect
from array import array
def task_func(n=10, total=100):
    """
    Generates 'n' random integer numbers such that their sum equals 'total', sorts these numbers, and determines the position where a new random number can be inserted to maintain the sorted order.
    The function uses a retry mechanism to ensure the generated numbers sum up to 'total'.
    The function should output with:
        tuple: A tuple containing the sorted numbers as an array and the insertion position for a new number.
    """
    # Generate 'n' random numbers
    numbers = [random.randint(1, total) for _ in range(n)]

    # Calculate the sum of the generated numbers
    sum_of_numbers = sum(numbers)

    # Check if the sum of the generated numbers is equal to 'total'
    if sum_of_numbers != total:
        # If not, retry with a new set of numbers
        return task_func(n, total)

    # Sort the generated numbers
    sorted_numbers = sorted(numbers)

    # Determine the position where a new random number can be inserted to maintain the sorted order
    insertion_position = bisect.bisect_left(sorted_numbers, random.randint(1, total))

    # Return the sorted numbers and the insertion position
    return (sorted_numbers, insertion_position)
n = 10
total = 100