
import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    if seed is not None:
        random.seed(seed)
    
    modified_list = []
    for item in data_list:
        # Find all substrings separated by commas
        substrings = item.split(',')
        # Remove a random substring
        if len(substrings) > 1:
            random_index = random.randint(0, len(substrings) - 1)
            modified_item = ','.join([substrings[i] for i in range(len(substrings)) if i != random_index])
        else:
            modified_item = item
        modified_list.append(modified_item)
    
    # Create a DataFrame
    df = pd.DataFrame({'Original String': data_list, 'Modified String': modified_list})
    return df