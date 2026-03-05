
import pandas as pd
import numpy as np

def task_func(column, data):
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if the specified column exists in the DataFrame
    if column not in df.columns:
        raise ValueError("Invalid column name")
    
    # Calculate the sum, mean, minimum, and maximum values for the specified column
    result = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    return result