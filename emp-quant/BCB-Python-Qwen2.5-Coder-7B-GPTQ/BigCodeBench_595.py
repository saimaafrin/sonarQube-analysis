import random
import bisect
from array import array
def task_func(n=10, total=100):
    while True:
        # Generate 'n' random integers
        numbers = [random.randint(1, total // n) for _ in range(n)]
        
        # Ensure the sum of numbers equals 'total'
        current_sum = sum(numbers)
        if current_sum == total:
            # Sort the numbers
            numbers.sort()
            
            # Generate a new random number
            new_number = random.randint(1, total // n)
            
            # Find the insertion position to maintain sorted order
            insertion_position = bisect.bisect_left(numbers, new_number)
            
            return (array('i', numbers), insertion_position)