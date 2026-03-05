
import numpy as np
import pandas as pd

def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Set the random seed if provided
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate a DataFrame with the specified number of rows and columns
    df = pd.DataFrame(np.random.randint(0, 101, size=(n_rows, len(columns))), columns=columns)
    
    # Remove the columns specified in remove_cols
    df = df.drop(columns=remove_cols)
    
    # Return the resulting DataFrame
    return df