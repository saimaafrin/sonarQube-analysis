
import itertools
import math

def task_func(x):
    # Initialize variables to store the minimum length and the corresponding sub-sequence
    min_length = math.inf
    min_subsequence = []
    
    # Iterate over all possible subsequences of the dictionary keys
    for r in range(1, len(x) + 1):
        for subsequence in itertools.combinations(x.keys(), r):
            # Calculate the total length of the current sub-sequence
            total_length = sum(x[key] for key in subsequence)
            # Update the minimum length and sub-sequence if the current one is smaller
            if total_length < min_length:
                min_length = total_length
                min_subsequence = list(subsequence)
    
    return min_subsequence