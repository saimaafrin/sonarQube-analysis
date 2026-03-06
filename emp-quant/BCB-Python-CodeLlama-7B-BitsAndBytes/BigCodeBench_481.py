
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    random.seed(seed)
    randomized_list = []
    for string in data_list:
        # Split the string into substrings using regex
        substrings = re.split(r',\s*', string)
        # Shuffle the substrings
        random.shuffle(substrings)
        # Join the substrings back into a string with a single space between each substring
        randomized_string = ' '.join(substrings)
        randomized_list.append(randomized_string)
    # Create a DataFrame with the original and randomized strings
    df = pd.DataFrame({'Original String': data_list, 'Randomized String': randomized_list})
    return df