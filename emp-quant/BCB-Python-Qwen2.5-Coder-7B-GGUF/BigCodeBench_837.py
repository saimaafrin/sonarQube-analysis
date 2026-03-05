
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Create a DataFrame with random values
    df = pd.DataFrame(np.random.rand(n_rows, len(columns)), columns=columns)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Scale the specified columns
    if scale_cols:
        df[scale_cols] = scaler.fit_transform(df[scale_cols])
    
    return df