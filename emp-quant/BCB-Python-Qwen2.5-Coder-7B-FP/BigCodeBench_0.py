import itertools
from random import shuffle
def task_func(numbers=list(range(1, 3))):
    """
    Calculates the average of the sums of absolute differences between each pair of consecutive numbers 
    for all permutations of a given list. Each permutation is shuffled before calculating the differences.
    
    Args:
    - numbers (list): A list of numbers. Default is numbers from 1 to 10.
    
    Returns:
    - float: The average of the sums of absolute differences for each shuffled permutation of the list.
    """
    total_sum = 0
    num_permutations = 1000  # Number of permutations to consider for the average
    
    for _ in range(num_permutations):
        shuffle(numbers)
        current_sum = sum(abs(numbers[i] - numbers[i+1]) for i in range(len(numbers)-1))
        total_sum += current_sum
    
    average_sum = total_sum / num_permutations
    return average_sum