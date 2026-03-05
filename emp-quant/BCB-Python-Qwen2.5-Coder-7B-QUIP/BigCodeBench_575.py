
from random import shuffle
import pandas as pd
import numpy as np
# Constants
def task_func(l, n_groups = 5):
    # Shuffle the list
    shuffle(l)
    
    # Create a DataFrame from the shuffled list
    df = pd.DataFrame(l, columns=['value'])
    
    # Function to move the first n_groups elements to the end of the row
    def move_elements(row):
        if len(row) > n_groups:
            return row[n_groups:] + row[:n_groups]
        return row
    
    # Apply the function to each row in the DataFrame
    df = df.apply(move_elements, axis=1)
    
    # Output the DataFrame
    print("DataFrame:")
    print(df)