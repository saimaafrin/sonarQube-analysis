import pandas as pd
import numpy as np
import itertools
def task_func(T1, row_num=50, seed=None):
    # Convert elements in 'T1' to integers
    num_cols = sum(int(x) for x, _ in T1)
    
    # Initialize the DataFrame with random numbers
    np.random.seed(seed)
    df = pd.DataFrame(np.random.randint(0, 100, size=(row_num, num_cols)), columns=[f'Col_{i+1}' for i in range(num_cols)])
    
    return df
T1 = (('1', '12'), ('1', '-12'))