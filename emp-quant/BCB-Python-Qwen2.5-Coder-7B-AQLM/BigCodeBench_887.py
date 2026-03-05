
import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    # Convert elements in 'T1' to integers
    int_values = [int(value) for sublist in T1 for value in sublist]
    
    # Calculate the number of columns based on the sum of integers in 'T1'
    num_columns = sum(int_values)
    
    # Set the seed for random number generation
    np.random.seed(seed)
    
    # Create a DataFrame with random numbers
    df = pd.DataFrame(np.random.randint(0, 100, size=(row_num, num_columns)), columns=[f'Col_{i+1}' for i in range(num_columns)])
    
    return df