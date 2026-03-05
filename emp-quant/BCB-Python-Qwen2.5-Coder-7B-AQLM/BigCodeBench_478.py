
import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    if seed is not None:
        random.seed(seed)
    
    modified_list = []
    for item in data_list:
        # Split the string by commas
        parts = item.split(',')
        # Remove a random part
        if len(parts) > 1:
            random_index = random.randint(0, len(parts) - 1)
            del parts[random_index]
        # Join the remaining parts back into a string
        modified_item = ','.join(parts)
        modified_list.append(modified_item)
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Original String': data_list,
        'Modified String': modified_list
    })
    
    return df