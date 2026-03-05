
import pandas as pd
import numpy as np

def task_func(data, cols):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    # Calculate the correlation matrix of the numeric columns
    correlation_matrix = df[numeric_cols].corr()
    
    return correlation_matrix