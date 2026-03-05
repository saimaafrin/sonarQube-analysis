
from itertools import combinations
import math

def task_func(seq, letter_weight_dict):
    # Calculate the weight of each letter in the sequence
    letter_weights = [letter_weight_dict[letter] for letter in seq]
    # Calculate the total weight of the sequence
    total_weight = sum(letter_weights)
    # Find the maximum weight subsequence
    max_weight_subsequence = max(combinations(seq, i), key=lambda x: sum(letter_weight_dict[letter] for letter in x))
    return max_weight_subsequence