from random import shuffle
import pandas as pd
import numpy as np
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a DataFrame from the shuffled list
    df = pd.DataFrame(l, columns=['Original'])
    
    # Function to rotate elements in each row
    def rotate_row(row, n):
        return row['Original'][n:] + row['Original'][:n]
    
    # Apply the rotation to each row
    df['Rotated'] = df.apply(rotate_row, args=(n_groups,), axis=1)
    
    # Drop the original column if not needed
    df = df[['Rotated']]
    
    return df