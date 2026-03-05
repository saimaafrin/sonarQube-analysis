from itertools import combinations
import math
def task_func(x, w):
    """
    Find the continuous substring of x, which has the maximum total weight, given a dictionary where the keys are characters and the values are their weights.
    The function should output with:
        max_substr (str): The continuous substring with the highest weight.
    """
    # Initialize variables
    max_substr = ""
    max_weight = 0

    # Iterate over all possible substrings
    for i in range(len(x)):
        for j in range(i, len(x)):
            substr = x[i:j+1]
            weight = sum(w[c] for c in substr)
            if weight > max_weight:
                max_substr = substr
                max_weight = weight

    return max_substr