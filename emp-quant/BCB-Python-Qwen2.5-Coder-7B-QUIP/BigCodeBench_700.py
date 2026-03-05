
import pandas as pd
import numpy as np

def task_func(data, cols):
    # Convert the data into a DataFrame
    df = pd.DataFrame(data, columns=cols)
    
    # Calculate the correlation matrix for the numeric columns
    correlation_matrix = df.corr()
    
    return correlation_matrix