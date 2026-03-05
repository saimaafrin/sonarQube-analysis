from random import shuffle
import pandas as pd
import numpy as np
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a DataFrame from the shuffled list
    df = pd.DataFrame(l, columns=['Original'])
    
    # Function to rotate the first n_groups elements to the end of the row
    def rotate_row(row, n_groups):
        return row['Original'][n_groups:] + row['Original'][:n_groups]
    
    # Apply the rotation to each row
    df['Rotated'] = df.apply(rotate_row, args=(n_groups,), axis=1)
    
    # Return the modified DataFrame
    return df[['Rotated']]