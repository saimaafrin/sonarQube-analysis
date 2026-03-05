import itertools
import math
def task_func(x):
    # Initialize variables to store the maximum sum and the corresponding key pair
    max_sum = float('-inf')
    max_pair = None
    
    # Iterate over all possible pairs of keys in the dictionary
    for pair in itertools.combinations(x.keys(), 2):
        # Calculate the sum of the cosine of the values for the current pair
        current_sum = math.cos(x[pair[0]]) + math.cos(x[pair[1]])
        
        # Update the maximum sum and the corresponding key pair if the current sum is higher
        if current_sum > max_sum:
            max_sum = current_sum
            max_pair = pair
    
    # Return the key pair with the highest sum of the cosine of their values
    return max_pair