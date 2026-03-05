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
    num_permutations = 0
    
    # Generate all permutations of the list
    for perm in itertools.permutations(numbers):
        # Shuffle the permutation
        shuffle(list(perm))
        
        # Calculate the sum of absolute differences between consecutive numbers
        perm_sum = sum(abs(perm[i] - perm[i+1]) for i in range(len(perm)-1))
        
        # Add to total sum and increment permutation count
        total_sum += perm_sum
        num_permutations += 1
    
    # Calculate the average
    average = total_sum / num_permutations if num_permutations > 0 else 0
    
    return average