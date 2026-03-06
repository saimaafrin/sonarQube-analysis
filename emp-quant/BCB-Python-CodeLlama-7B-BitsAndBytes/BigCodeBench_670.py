
from itertools import combinations
import math

def task_func(x, w):
    # Find the maximum total weight of a substring
    max_weight = 0
    max_substr = ""
    for i in range(len(x)):
        for j in range(i, len(x)):
            substr = x[i:j+1]
            weight = sum(w[c] for c in substr)
            if weight > max_weight:
                max_weight = weight
                max_substr = substr
    return max_substr