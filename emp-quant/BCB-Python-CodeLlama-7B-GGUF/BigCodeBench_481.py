
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    random.seed(seed)

    # Create a list of tuples containing the original and randomized strings
    data = [(original_string, randomize_string(original_string)) for original_string in data_list]

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=['Original String', 'Randomized String'])

    return df

def randomize_string(string):
    # Split the string into a list of substrings separated by commas
    substrings = string.split(',')

    # Randomize the order of the substrings
    random.shuffle(substrings)

    # Join the substrings back together with a comma and a space
    randomized_string = ', '.join(substrings)

    # Normalize the spaces to ensure a single space follows each comma
    randomized_string = re.sub(r'\s+', ' ', randomized_string)

    return randomized_string