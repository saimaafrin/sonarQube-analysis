import random
import bisect
from array import array
def task_func(n=10, total=100):
    while True:
        # Generate 'n' random integers that sum up to 'total'
        numbers = [random.randint(1, total) for _ in range(n-1)]
        numbers.append(total - sum(numbers))
        
        # Sort the numbers
        numbers.sort()
        
        # Find the insertion position for a new random number
        new_number = random.randint(1, total)
        insertion_position = bisect.bisect(numbers, new_number)
        
        # Return the sorted numbers and the insertion position
        return (array('i', numbers), insertion_position)