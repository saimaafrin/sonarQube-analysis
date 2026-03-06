
from itertools import combinations
import math

def task_func(seq, letter_weight_dict):
    # Initialize variables to keep track of the maximum weight and the corresponding subsequence
    max_weight = 0
    max_subsequence = ""

    # Iterate over all possible substrings of the input sequence
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            # Calculate the weight of the current substring
            weight = 0
            for k in range(i, j):
                weight += letter_weight_dict[seq[k]]

            # If the current substring has a higher weight than the previous maximum, update the maximum weight and subsequence
            if weight > max_weight:
                max_weight = weight
                max_subsequence = seq[i:j+1]

    return max_subsequence