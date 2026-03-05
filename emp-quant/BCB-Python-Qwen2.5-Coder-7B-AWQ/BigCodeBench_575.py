from random import shuffle
import pandas as pd
import numpy as np
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a DataFrame from the shuffled list
    df = pd.DataFrame(l, columns=['Values'])
    
    # Split each row into n_groups and move the first n_groups elements to the end
    def rotate_row(row, n):
        return row['Values'][n:] + row['Values'][:n]
    
    df['Values'] = df.apply(lambda row: rotate_row(row, n_groups), axis=1)
    
    return df