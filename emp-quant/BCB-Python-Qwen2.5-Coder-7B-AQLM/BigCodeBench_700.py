
import pandas as pd
import numpy as np

def task_func(data, cols):
    # Convert the provided data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Filter out non-numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Calculate the correlation matrix of numeric columns
    correlation_matrix = numeric_df.corr()
    
    return correlation_matrix