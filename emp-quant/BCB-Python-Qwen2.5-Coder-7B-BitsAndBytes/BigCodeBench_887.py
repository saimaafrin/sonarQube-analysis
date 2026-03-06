
import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    # Convert elements in 'T1' to integers
    int_values = [int(item) for sublist in T1 for item in sublist]
    
    # Calculate the total number of columns
    num_columns = sum(int_values)
    
    # Set the random seed if provided
    if seed is not None:
        np.random.seed(seed)
    
    # Create a DataFrame with random numbers
    data = np.random.randint(0, 100, size=(row_num, num_columns))
    columns = ['Col_' + str(i+1) for i in range(num_columns)]
    df = pd.DataFrame(data, columns=columns)
    
    return df