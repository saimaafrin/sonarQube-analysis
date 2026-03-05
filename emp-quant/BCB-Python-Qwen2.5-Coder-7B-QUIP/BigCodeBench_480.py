
import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    # Set the seed for random shuffling
    if seed is not None:
        random.seed(seed)
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each string in the input list
    for item in data_list:
        # Split the string into substrings based on commas
        substrings = re.split(r'\s*,\s*', item)
        
        # Shuffle the substrings
        random.shuffle(substrings)
        
        # Join the shuffled substrings back into a single string
        shuffled_item = ', '.join(substrings)
        
        # Append the original and shuffled strings to the results list
        results.append({'Original String': item, 'Shuffled String': shuffled_item})
    
    # Convert the results list to a pandas DataFrame
    df = pd.DataFrame(results)
    
    # Return the DataFrame
    return df