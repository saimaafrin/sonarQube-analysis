
from random import shuffle
import pandas as pd
import numpy as np

# Constants
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a DataFrame from the shuffled list
    df = pd.DataFrame(l, columns=['Values'])
    
    # Function to rotate elements in each row
    def rotate_row(row, n_groups):
        return row['Values'][n_groups:] + row['Values'][:n_groups]
    
    # Apply the rotation to each row
    df['Rotated'] = df.apply(rotate_row, args=(n_groups,), axis=1)
    
    # Drop the original column and rename the rotated column
    df = df.drop(columns=['Values']).rename(columns={'Rotated': 'Values'})
    
    return df