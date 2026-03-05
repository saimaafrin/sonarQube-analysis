
import numpy as np
import pandas as pd
import random

def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Create a matrix of random integers
    matrix = np.random.randint(min_val, max_val, size=(rows, cols))
    
    # Convert the matrix to a pandas DataFrame
    df = pd.DataFrame(matrix, columns=[f"col{col}" for col in range(1, cols + 1)])
    
    # Output the DataFrame
    print("DataFrame:")
    print(df)
    
    # Return the DataFrame
    return df