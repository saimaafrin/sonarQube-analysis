
import pandas as pd
import numpy as np

def task_func(data, cols):
    # Convert the input data to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Select only the specified columns from the DataFrame
    selected_df = df[cols]
    
    # Calculate the correlation matrix for the selected columns
    correlation_matrix = selected_df.corr()
    
    return correlation_matrix