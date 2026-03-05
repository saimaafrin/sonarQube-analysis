from itertools import combinations
import math
def task_func(seq, letter_weight_dict):
    # Initialize variables to store the maximum weight and the corresponding subsequence
    max_weight = -math.inf
    max_subsequence = ""
    
    # Iterate over all possible lengths of subsequences
    for r in range(1, len(seq) + 1):
        # Generate all combinations of the current length
        for combo in combinations(seq, r):
            # Calculate the weight of the current subsequence
            current_weight = sum(letter_weight_dict[char] for char in combo)
            # Update the maximum weight and subsequence if the current one is heavier
            if current_weight > max_weight:
                max_weight = current_weight
                max_subsequence = ''.join(combo)
    
    # Return the subsequence with the highest weight
    return max_subsequence