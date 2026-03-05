
from random import shuffle
import pandas as pd
import numpy as np
# Constants
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Construct a DataFrame from the shuffled list
    df = pd.DataFrame(l, columns=['Original'])
    
    # Function to rotate the first n_groups elements to the end of the row
    def rotate_row(row, n_groups):
        return row['Original'][n_groups:] + row['Original'][:n_groups]
    
    # Apply the rotation to each row
    df['Rotated'] = df.apply(rotate_row, axis=1, n_groups=n_groups)
    
    # Return the modified DataFrame
    return df