
import re
import random
import pandas as pd

def task_func(data_list, seed=None):
    if seed is not None:
        random.seed(seed)
    
    shuffled_data = []
    for item in data_list:
        # Split the string by commas and strip whitespace
        substrings = [sub.strip() for sub in re.split(r',\s*', item)]
        # Shuffle the substrings
        random.shuffle(substrings)
        # Join the shuffled substrings back into a single string
        shuffled_item = ', '.join(substrings)
        shuffled_data.append((item, shuffled_item))
    
    # Create a DataFrame
    df = pd.DataFrame(shuffled_data, columns=['Original String', 'Shuffled String'])
    return df