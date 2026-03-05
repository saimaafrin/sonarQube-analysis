
import itertools
from random import shuffle

def task_func(numbers=list(range(1, 11))):
    """
    Calculates the average of the sums of absolute differences between each pair of consecutive numbers for all permutations of a given list.
    Each permutation is shuffled before calculating the differences.

    Args:
        numbers (list): A list of numbers. Default is numbers from 1 to 10.

    Returns:
        float: The average of the sums of absolute differences for each shuffled permutation of the list.
    """
    # Calculate the sums of absolute differences for each permutation
    sums_of_abs_diffs = []
    for perm in itertools.permutations(numbers):
        shuffle(perm)
        sum_of_abs_diffs = 0
        for i in range(len(perm) - 1):
            sum_of_abs_diffs += abs(perm[i] - perm[i + 1])
        sums_of_abs_diffs.append(sum_of_abs_diffs)

    # Calculate the average of the sums of absolute differences
    return sum(sums_of_abs_diffs) / len(sums_of_abs_diffs)