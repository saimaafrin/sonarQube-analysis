
import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    if seed is not None:
        random.seed(seed)
    
    modified_data = []
    for item in data_list:
        # Find all substrings separated by commas
        substrings = re.split(r',\s*', item)
        if len(substrings) > 1:
            # Randomly choose one substring to remove
            index_to_remove = random.randint(0, len(substrings) - 1)
            modified_item = ','.join([substrings[i] for i in range(len(substrings)) if i != index_to_remove])
        else:
            modified_item = item
        
        modified_data.append((item, modified_item))
    
    # Create a DataFrame
    df = pd.DataFrame(modified_data, columns=['Original String', 'Modified String'])
    return df