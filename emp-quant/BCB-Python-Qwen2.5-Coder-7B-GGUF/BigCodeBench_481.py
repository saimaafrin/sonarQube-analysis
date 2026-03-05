
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize lists to store original and randomized strings
    original_strings = []
    randomized_strings = []
    
    # Iterate over each string in the input list
    for data in data_list:
        # Split the string by commas and normalize spaces
        substrings = re.split(r'\s*,\s*', data)
        
        # Shuffle the list of substrings
        random.shuffle(substrings)
        
        # Join the shuffled substrings back into a single string with a single space after each comma
        randomized_string = ', '.join(substrings)
        
        # Append the original and randomized strings to the respective lists
        original_strings.append(data)
        randomized_strings.append(randomized_string)
    
    # Create a DataFrame with the original and randomized strings
    result_df = pd.DataFrame({
        'Original String': original_strings,
        'Randomized String': randomized_strings
    })
    
    return result_df