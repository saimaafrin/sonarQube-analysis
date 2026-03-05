
import random
import string
import pandas as pd

def task_func(data_list, seed=0):
    random.seed(seed)  # Set seed for reproducibility
    result = []
    for item in data_list:
        # Split the string into parts based on commas
        parts = item.split(',')
        # Replace a random part with a random string of the same length
        if ',' in item:
            index = random.randint(0, len(parts) - 1)
            parts[index] = ''.join(random.choices(string.ascii_lowercase, k=len(parts[index])))
        else:
            parts[0] = ''.join(random.choices(string.ascii_lowercase, k=len(item)))
        result.append(''.join(parts))
    # Create a DataFrame with 'Original String' and 'Modified String' columns
    df = pd.DataFrame({'Original String': data_list, 'Modified String': result})
    return df