
from itertools import combinations
import math

def task_func(x, w):
    # Find the longest substring with the highest weight
    max_substr = ""
    max_weight = 0
    for i in range(len(x)):
        for j in range(i, len(x)):
            substr = x[i:j+1]
            weight = sum(w[c] for c in substr)
            if weight > max_weight:
                max_substr = substr
                max_weight = weight
    return max_substr