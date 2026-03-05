
import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    # Set the seed for random number generation
    if seed is not None:
        random.seed(seed)

    # Initialize an empty list to store the modified strings
    modified_strings = []

    # Iterate over each string in the data_list
    for string in data_list:
        # Split the string by commas
        parts = string.split(',')
        # Remove a random part
        parts.remove(random.choice(parts))
        # Join the remaining parts back into a string
        modified_string = ','.join(parts)
        # Append the modified string to the list
        modified_strings.append(modified_string)

    # Create a pandas DataFrame with the original and modified strings
    df = pd.DataFrame({'Original String': data_list, 'Modified String': modified_strings})

    # Return the DataFrame
    return df