
import random
import bisect
from array import array

def task_func(n=10, total=100):
    while True:
        numbers = array('i', [random.randint(1, total) for _ in range(n)])
        if sum(numbers) == total:
            numbers.sort()
            insertion_position = bisect.bisect_left(numbers, random.randint(1, total))
            return numbers, insertion_position