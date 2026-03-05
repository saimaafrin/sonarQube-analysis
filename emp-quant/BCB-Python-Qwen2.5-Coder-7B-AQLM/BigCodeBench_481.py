
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    random.seed(seed)
    result = []
    for item in data_list:
        # Normalize spaces and split by comma
        substrings = re.split(r'\s*,\s*', item)
        # Randomize the order of substrings
        random.shuffle(substrings)
        # Join the substrings back into a single string with a single space after each comma
        randomized_item = ', '.join(substrings)
        result.append({'Original String': item, 'Randomized String': randomized_item})
    return pd.DataFrame(result)