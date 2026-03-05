
import numpy as np
import pandas as pd

def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Create a DataFrame with random integer values
    df = pd.DataFrame(np.random.randint(0, 101, size=(n_rows, len(columns))), columns=columns)
    
    # Remove specified columns
    df = df.drop(columns=columns[remove_cols])
    
    return df