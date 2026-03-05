
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the DataFrame contains NaN values
    if df.isnull().values.any():
        raise ValueError("The DataFrame contains NaN values.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Create a copy of the DataFrame to store the results
    result_df = df.copy()
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Check if the column is numeric
        if np.issubdtype(df[column].dtype, np.number):
            # Compute the cumulative sum of the column
            cumsum = df[column].cumsum()
            # Fit and transform the cumulative sum using MinMaxScaler
            normalized_cumsum = scaler.fit_transform(cumsum.values.reshape(-1, 1)).flatten()
            # Assign the normalized cumulative sum back to the result DataFrame
            result_df[column] = normalized_cumsum
        else:
            raise TypeError(f"Column '{column}' contains non-numeric data types.")
    
    return result_df