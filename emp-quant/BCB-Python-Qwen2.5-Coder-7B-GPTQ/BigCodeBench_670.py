from itertools import combinations
import math
def task_func(x, w):
    max_weight = -math.inf
    max_substr = ""
    
    # Iterate over all possible substrings
    for start in range(len(x)):
        for end in range(start + 1, len(x) + 1):
            substring = x[start:end]
            # Calculate the total weight of the substring
            total_weight = sum(w[char] for char in substring)
            # Update the maximum weight and substring if the current one is greater
            if total_weight > max_weight:
                max_weight = total_weight
                max_substr = substring
    
    return max_substr