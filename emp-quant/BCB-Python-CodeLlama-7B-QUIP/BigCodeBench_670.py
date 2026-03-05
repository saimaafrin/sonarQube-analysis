
from itertools import combinations
import math

def task_func(x, w):
    # Find the maximum total weight of any substring
    max_weight = -1
    max_substr = ""
    for i in range(len(x)):
        for j in range(i, len(x)):
            substr = x[i:j+1]
            weight = w[substr[0]]
            for c in substr:
                weight += w[c]
            if weight > max_weight:
                max_weight = weight
                max_substr = substr
    return max_substr