import pandas as pd
import numpy as np
import itertools
def task_func(T1, row_num=50, seed=None):
    # Convert elements in 'T1' to integers
    int_values = [int(item) for sublist in T1 for item in sublist]
    
    # Calculate the total number of columns
    total_columns = sum(int_values)
    
    # Set the random seed if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Create a DataFrame with random numbers
    df = pd.DataFrame(np.random.randint(0, 100, size=(row_num, total_columns)), columns=[f'Col_{i+1}' for i in range(total_columns)])
    
    return df
T1 = (('1', '12'), ('1', '-12'))