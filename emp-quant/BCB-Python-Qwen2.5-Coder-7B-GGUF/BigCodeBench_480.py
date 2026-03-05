
import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    # Set the seed for random shuffling if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize lists to store original and shuffled strings
    original_strings = []
    shuffled_strings = []
    
    # Iterate over each string in the input list
    for item in data_list:
        # Split the string by commas and strip whitespace
        substrings = [sub.strip() for sub in item.split(',')]
        
        # Shuffle the substrings
        random.shuffle(substrings)
        
        # Join the shuffled substrings back into a single string
        shuffled_string = ', '.join(substrings)
        
        # Append the original and shuffled strings to the respective lists
        original_strings.append(item)
        shuffled_strings.append(shuffled_string)
    
    # Create a pandas DataFrame with the original and shuffled strings
    result_df = pd.DataFrame({
        'Original String': original_strings,
        'Shuffled String': shuffled_strings
    })
    
    return result_df