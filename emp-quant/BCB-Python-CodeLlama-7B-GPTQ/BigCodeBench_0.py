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
    permutations = itertools.permutations(numbers)
    sums_of_diffs = [sum(abs(a - b) for a, b in zip(p, p[1:])) for p in permutations]

    # Shuffle each permutation and calculate the sums of absolute differences again
    shuffled_permutations = [shuffle(p) for p in permutations]
    shuffled_sums_of_diffs = [sum(abs(a - b) for a, b in zip(p, p[1:])) for p in shuffled_permutations]

    # Calculate the average of the sums of absolute differences for each shuffled permutation
    average_sums_of_diffs = sum(shuffled_sums_of_diffs) / len(shuffled_sums_of_diffs)

    return average_sums_of_diffs