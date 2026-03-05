
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Set the random seed for reproducibility
    if random_seed is not None:
        np.random.seed(random_seed)
    
    # Generate a DataFrame with random values
    data = pd.DataFrame(np.random.randint(1, 100, size=(n_rows, len(columns))), columns=columns)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Scale the specified columns
    if scale_cols:
        data[scale_cols] = scaler.fit_transform(data[scale_cols])
    
    # Return the resulting DataFrame
    return data