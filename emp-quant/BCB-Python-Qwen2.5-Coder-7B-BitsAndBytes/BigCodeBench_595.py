
import random
import bisect
from array import array

def task_func(n=10, total=100):
    def generate_numbers():
        numbers = [random.randint(1, total) for _ in range(n)]
        while sum(numbers) != total:
            numbers = [random.randint(1, total) for _ in range(n)]
        return numbers

    numbers = generate_numbers()
    numbers.sort()
    new_number = random.randint(1, total)
    insertion_position = bisect.bisect_left(numbers, new_number)

    return (array('i', numbers), insertion_position)