
from itertools import combinations
import math

def task_func(x, w):
    max_weight = -math.inf
    max_substr = ""

    for start, end in combinations(range(len(x) + 1), 2):
        substr = x[start:end]
        substr_weight = sum(w[char] for char in substr)
        if substr_weight > max_weight:
            max_weight = substr_weight
            max_substr = substr

    return max_substr