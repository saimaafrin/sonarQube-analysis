
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each string in the input list
    for data in data_list:
        # Normalize spaces around commas
        normalized_data = re.sub(r'\s*,\s*', ', ', data.strip())
        
        # Split the string into substrings based on commas
        substrings = normalized_data.split(', ')
        
        # Shuffle the order of substrings randomly
        random.shuffle(substrings)
        
        # Join the shuffled substrings back into a single string
        randomized_data = ', '.join(substrings)
        
        # Append the original and randomized strings to the results list
        results.append({'Original String': data, 'Randomized String': randomized_data})
    
    # Create a DataFrame from the results list
    df = pd.DataFrame(results)
    
    return df