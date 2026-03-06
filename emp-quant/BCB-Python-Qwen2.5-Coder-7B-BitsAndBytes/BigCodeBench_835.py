
import numpy as np
import pandas as pd

def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Create a DataFrame with random integers between 0 and 100
    data = {col: np.random.randint(0, 101, n_rows) for col in columns}
    df = pd.DataFrame(data)
    
    # Remove specified columns
    df = df.drop(columns=[columns[i] for i in remove_cols])
    
    return df