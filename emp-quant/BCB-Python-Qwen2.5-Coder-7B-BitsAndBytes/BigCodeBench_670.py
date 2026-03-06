
from itertools import combinations
import math

def task_func(x, w):
    """
    Find the continuous substring of x, which has the maximum total weight,
    given a dictionary where the keys are characters and the values are their weights.
    
    Parameters:
    x (str): The input string to find the substring from.
    w (dict): A dictionary with characters as keys and their weights as values.
    
    Returns:
    max_substr (str): The continuous substring with the highest weight.
    """
    if not x or not w:
        return ""
    
    max_weight = -math.inf
    max_substr = ""
    
    for start in range(len(x)):
        current_weight = 0
        for end in range(start, len(x)):
            current_weight += w.get(x[end], 0)
            if current_weight > max_weight:
                max_weight = current_weight
                max_substr = x[start:end+1]
    
    return max_substr