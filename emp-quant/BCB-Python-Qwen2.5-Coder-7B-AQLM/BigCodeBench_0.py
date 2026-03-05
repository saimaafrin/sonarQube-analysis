
import itertools
from random import shuffle

def task_func(numbers=list(range(1, 3))):
    def sum_of_absolute_differences(perm):
        return sum(abs(perm[i] - perm[i + 1]) for i in range(len(perm) - 1))
    
    total_sum = 0
    num_permutations = 1000  # Number of permutations to shuffle and calculate
    
    for _ in range(num_permutations):
        shuffle(numbers)
        total_sum += sum_of_absolute_differences(numbers)
    
    average = total_sum / num_permutations
    return average