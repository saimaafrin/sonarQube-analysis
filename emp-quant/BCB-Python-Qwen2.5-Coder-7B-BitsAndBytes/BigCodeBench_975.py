
import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Create a DataFrame with random values
    data = np.random.rand(rows, len(columns))
    df = pd.DataFrame(data, columns=columns)
    
    # Shuffle the columns
    df = df[columns[np.random.permutation(len(columns))]]
    
    return df