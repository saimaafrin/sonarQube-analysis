from itertools import combinations
import math
def task_func(x, w):
    # Initialize variables to store the maximum weight and the corresponding substring
    max_weight = -math.inf
    max_substr = ""
    
    # Iterate over all possible substrings of x
    for start in range(len(x)):
        for end in range(start + 1, len(x) + 1):
            # Calculate the weight of the current substring
            current_weight = sum(w[char] for char in x[start:end])
            # Update the maximum weight and substring if the current one is higher
            if current_weight > max_weight:
                max_weight = current_weight
                max_substr = x[start:end]
    
    return max_substr