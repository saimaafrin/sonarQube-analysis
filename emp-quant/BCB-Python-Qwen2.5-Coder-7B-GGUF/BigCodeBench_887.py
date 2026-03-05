
import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    # Convert elements in 'T1' to integers
    num_columns = sum(int(item) for sublist in T1 for item in sublist)
    
    # Set the seed for random number generation
    np.random.seed(seed)
    
    # Create a DataFrame with random numbers
    df = pd.DataFrame(np.random.randint(0, 100, size=(row_num, num_columns)), columns=[f'Col_{i+1}' for i in range(num_columns)])
    
    return df