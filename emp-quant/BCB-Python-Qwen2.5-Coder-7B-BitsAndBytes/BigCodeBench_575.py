
from random import shuffle
import pandas as pd
import numpy as np

# Constants
def task_func(l, n_groups=5):
    # Shuffle the list
    shuffle(l)
    
    # Create a DataFrame from the shuffled list
    df = pd.DataFrame(l, columns=['Values'])
    
    # Split each row into groups and rearrange
    def rearrange_row(row):
        values = row['Values']
        if len(values) > n_groups:
            return np.concatenate((values[n_groups:], values[:n_groups]))
        else:
            return values
    
    df['Values'] = df.apply(rearrange_row, axis=1)
    
    return df