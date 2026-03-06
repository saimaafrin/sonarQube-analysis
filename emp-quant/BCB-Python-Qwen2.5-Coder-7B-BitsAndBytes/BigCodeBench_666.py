
from itertools import combinations
import math

def task_func(seq, letter_weight_dict):
    max_weight = -math.inf
    best_subsequence = ""
    
    # Iterate over all possible subsequences
    for r in range(1, len(seq) + 1):
        for subseq in combinations(seq, r):
            current_weight = sum(letter_weight_dict[char] for char in subseq)
            if current_weight > max_weight:
                max_weight = current_weight
                best_subsequence = ''.join(subseq)
                
    return best_subsequence