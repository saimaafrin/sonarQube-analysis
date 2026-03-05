
import itertools
from random import shuffle
def task_func(numbers=list(range(1, 3))):
    def calculate_sum_of_differences(perm):
        shuffle(perm)
        return sum(abs(perm[i] - perm[i+1]) for i in range(len(perm)-1))

    total_sum = 0
    num_permutations = len(list(itertools.permutations(numbers)))
    for perm in itertools.permutations(numbers):
        total_sum += calculate_sum_of_differences(perm)

    return total_sum / num_permutations