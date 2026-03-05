
import random
import numpy as np

def task_func(LETTERS):
    # Initialize an empty dictionary to store the results
    result = {}
    
    # Iterate over each letter in the input list
    for letter in LETTERS:
        # Generate a random list of integers between 0 and 100
        random_list = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
        
        # Calculate the mean of the random list
        mean_value = np.mean(random_list)
        
        # Store the mean value in the result dictionary
        result[letter] = mean_value
    
    # Return the result dictionary
    return result