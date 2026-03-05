import re
import random
import pandas as pd
def task_func(data_list, seed=None):
    # Set the seed for random shuffling if provided
    if seed is not None:
        random.seed(seed)
    
    # Initialize an empty list to store the shuffled strings
    shuffled_strings = []
    
    # Iterate over each string in the input list
    for item in data_list:
        # Split the string by commas and strip whitespace
        substrings = [sub.strip() for sub in re.split(r',\s*', item)]
        
        # Shuffle the substrings
        random.shuffle(substrings)
        
        # Join the shuffled substrings back into a single string
        shuffled_string = ', '.join(substrings)
        
        # Append the original and shuffled strings to the list
        shuffled_strings.append((item, shuffled_string))
    
    # Create a pandas DataFrame from the list of tuples
    result_df = pd.DataFrame(shuffled_strings, columns=['Original String', 'Shuffled String'])
    
    return result_df