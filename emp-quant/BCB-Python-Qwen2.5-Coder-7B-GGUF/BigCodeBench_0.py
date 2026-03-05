
import itertools
from random import shuffle

def task_func(numbers=list(range(1, 3))):
    total_sum = 0
    num_permutations = 1000  # Number of permutations to consider
    
    for _ in range(num_permutations):
        shuffle(numbers)
        permutation_sum = 0
        for i in range(len(numbers) - 1):
            permutation_sum += abs(numbers[i] - numbers[i + 1])
        total_sum += permutation_sum
    
    average_sum = total_sum / num_permutations
    return average_sum