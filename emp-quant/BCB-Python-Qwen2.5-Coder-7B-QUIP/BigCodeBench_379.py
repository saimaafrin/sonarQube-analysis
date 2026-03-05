
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

def task_func(length):
    # Generate random data
    data = np.random.rand(length, len(COLUMNS))
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Output the DataFrame
    print("DataFrame:")
    print(df)