
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize an empty list to store the results
    results = []

    # Iterate over each string in the input list
    for string in data_list:
        # Normalize spaces to ensure a single space follows each comma
        normalized_string = re.sub(r',\s*', ', ', string)

        # Split the normalized string into substrings
        substrings = normalized_string.split(', ')

        # Randomize the order of the substrings
        random.shuffle(substrings)

        # Join the randomized substrings back into a single string
        randomized_string = ', '.join(substrings)

        # Append the original and randomized strings to the results list
        results.append({'Original String': string, 'Randomized String': randomized_string})

    # Convert the results list to a pandas DataFrame
    df = pd.DataFrame(results)

    # Return the DataFrame
    return df