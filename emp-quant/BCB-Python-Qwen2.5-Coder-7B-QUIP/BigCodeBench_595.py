
import random
import bisect
from array import array

def task_func(n=10, total=100):
    def generate_numbers(n, total):
        numbers = [random.randint(1, 10) for _ in range(n)]
        while sum(numbers) != total:
            numbers = [random.randint(1, 10) for _ in range(n)]
        return numbers

    def find_insertion_position(numbers, new_number):
        bisect.insort(numbers, new_number)
        return numbers, bisect.bisect(numbers, new_number)

    numbers = generate_numbers(n, total)
    new_number = random.randint(1, 10)
    sorted_numbers, insertion_position = find_insertion_position(numbers, new_number)
    return tuple(sorted_numbers), insertion_position