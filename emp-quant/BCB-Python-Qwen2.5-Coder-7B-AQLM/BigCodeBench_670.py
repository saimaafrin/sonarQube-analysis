
from itertools import combinations
import math

def task_func(x, w):
    max_weight = -math.inf
    max_substr = ""
    
    for start in range(len(x)):
        current_weight = 0
        for end in range(start, len(x)):
            current_weight += w[x[end]]
            if current_weight > max_weight:
                max_weight = current_weight
                max_substr = x[start:end+1]
    
    return max_substr