
import numpy as np
import pandas as pd
# Constants
RANGE = (1, 100)

def task_func(L):
    # Calculate the number of rows and columns based on the input list of lists
    num_rows = np.prod([len(row) for row in L])
    num_cols = np.prod([len(col) for col in L[0]])
    
    # Generate a DataFrame with random integers within the specified range
    data = np.random.randint(RANGE[0], RANGE[1], size=(num_rows, num_cols))
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame(data)
    
    # Output the DataFrame
    print("DataFrame:")
    print(df)