
import numpy as np
import pandas as pd
import random

def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    # Create a matrix of specified dimensions with random integers within a given range
    matrix = np.random.randint(min_val, max_val, size=(rows, cols), dtype=int)

    # Convert the matrix into a pandas DataFrame
    df = pd.DataFrame(matrix)

    # Output the DataFrame
    print(df)

# Call the function with the specified parameters
task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0)