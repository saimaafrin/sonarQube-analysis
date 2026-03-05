
import random
import bisect
from array import array

def task_func(n=10, total=100):
    def generate_random_numbers(n, total):
        numbers = []
        for i in range(n):
            numbers.append(random.randint(1, total))
        return numbers

    def get_sorted_numbers(numbers):
        return sorted(numbers)

    def get_insertion_position(numbers, new_number):
        for i in range(len(numbers)):
            if numbers[i] > new_number:
                return i
        return len(numbers)

    def retry_generate_random_numbers(n, total):
        numbers = generate_random_numbers(n, total)
        if sum(numbers) != total:
            return retry_generate_random_numbers(n, total)
        return numbers

    numbers = retry_generate_random_numbers(n, total)
    sorted_numbers = get_sorted_numbers(numbers)
    insertion_position = get_insertion_position(sorted_numbers, random.randint(1, total))
    return (sorted_numbers, insertion_position)