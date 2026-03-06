
import itertools
from random import shuffle

def calculate_sum_of_differences(numbers):
    n = len(numbers)
    total_difference = 0
    for i in range(n - 1):
        total_difference += abs(numbers[i] - numbers[i + 1])
    return total_difference

def task_func(numbers=list(range(1, 3))):
    if not numbers:
        return 0.0
    
    num_permutations = factorial(len(numbers))
    total_average_difference = 0.0
    
    for _ in range(num_permutations):
        shuffle(numbers)
        total_average_difference += calculate_sum_of_differences(numbers)
    
    return total_average_difference / num_permutations

# Helper function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)