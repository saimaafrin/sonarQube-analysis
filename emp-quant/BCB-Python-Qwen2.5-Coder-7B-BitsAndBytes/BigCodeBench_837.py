
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Create a DataFrame with random values
    data = {col: np.random.randn(n_rows) for col in columns}
    df = pd.DataFrame(data)
    
    # Check if there are any columns to scale
    if scale_cols:
        scaler = StandardScaler()
        df[scale_cols] = scaler.fit_transform(df[scale_cols])
    
    return df