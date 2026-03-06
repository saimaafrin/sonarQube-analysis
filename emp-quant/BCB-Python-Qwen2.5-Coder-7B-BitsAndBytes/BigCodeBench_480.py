
import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    # Set the seed for reproducibility if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each string in the input list
    for item in data_list:
        # Split the string by commas and strip whitespace
        substrings = [sub.strip() for sub in re.split(r',\s*', item)]
        
        # Shuffle the substrings
        random.shuffle(substrings)
        
        # Join the shuffled substrings back into a single string
        shuffled_string = ', '.join(substrings)
        
        # Append the original and shuffled strings to the result list
        result.append({'Original String': item, 'Shuffled String': shuffled_string})
    
    # Create a pandas DataFrame from the result list
    df = pd.DataFrame(result)
    
    return df