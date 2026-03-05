import pandas as pd
import re
import random
def task_func(data_list, seed=None):
    if seed is not None:
        random.seed(seed)
    
    modified_list = []
    for item in data_list:
        # Find all comma-separated values
        values = re.split(r',\s*', item)
        if len(values) > 1:
            # Remove a random value
            values.remove(random.choice(values))
        # Join the remaining values back into a string
        modified_item = ', '.join(values)
        modified_list.append(modified_item)
    
    # Create a DataFrame with original and modified strings
    df = pd.DataFrame({
        'Original String': data_list,
        'Modified String': modified_list
    })
    
    return df