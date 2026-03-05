
import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random values for the DataFrame
    data = np.random.rand(rows, len(columns))
    
    # Create a DataFrame with the generated data
    df = pd.DataFrame(data, columns=columns)
    
    # Shuffle the columns in ascending order
    df = df[columns[np.random.permutation(len(columns))]]
    
    return df