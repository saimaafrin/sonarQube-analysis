
import random
import bisect
from array import array

def task_func(n=10, total=100):
    # Generate 'n' random integers
    nums = [random.randint(1, total) for _ in range(n)]

    # Sort the numbers
    nums.sort()

    # Determine the position where a new random number can be inserted to maintain the sorted order
    insert_pos = bisect.bisect_left(nums, random.randint(1, total))

    return (nums, insert_pos)