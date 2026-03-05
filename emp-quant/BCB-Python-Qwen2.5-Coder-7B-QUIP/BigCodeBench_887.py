
import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    # Convert elements in 'T1' to integers
    T1 = tuple(int(x) for x in itertools.chain.from_iterable(T1))
    
    # Calculate the number of columns in the DataFrame
    num_columns = sum(T1)
    
    # Set the seed for the random number generator
    if seed is not None:
        np.random.seed(seed)
    
    # Create a DataFrame with random numbers
    df = pd.DataFrame(np.random.randint(0, 100, size=(row_num, num_columns)))
    
    # Rename the columns
    df.columns = [f"Col_{i+1}" for i in range(num_columns)]
    
    return df