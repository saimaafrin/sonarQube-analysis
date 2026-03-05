from itertools import combinations
import math
def task_func(seq, letter_weight_dict):
    # Initialize variables to store the maximum weight and the corresponding subsequence
    max_weight = -math.inf
    best_subsequence = ""
    
    # Iterate over all possible subsequences of the input sequence
    for r in range(1, len(seq) + 1):
        for subseq in combinations(seq, r):
            # Calculate the total weight of the current subsequence
            current_weight = sum(letter_weight_dict[char] for char in subseq)
            # Update the maximum weight and best subsequence if the current one is better
            if current_weight > max_weight:
                max_weight = current_weight
                best_subsequence = ''.join(subseq)
    
    # Return the subsequence with the highest weight
    return best_subsequence