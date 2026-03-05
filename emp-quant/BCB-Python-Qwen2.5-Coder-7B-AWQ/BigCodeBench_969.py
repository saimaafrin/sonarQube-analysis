import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Create a copy of the DataFrame to store the results
    result_df = df.copy()
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Check if the column contains non-numeric data types
        if not pd.api.types.is_numeric_dtype(df[column]):
            raise TypeError(f"Column '{column}' contains non-numeric data types.")
        
        # Check if the column contains NaN values
        if df[column].isnull().any():
            raise ValueError(f"Column '{column}' contains NaN values.")
        
        # Compute the cumulative sum of the column
        cumulative_sum = df[column].cumsum()
        
        # Fit and transform the cumulative sum using MinMaxScaler
        scaled_cumulative_sum = scaler.fit_transform(cumulative_sum.values.reshape(-1, 1))
        
        # Assign the scaled cumulative sum back to the result DataFrame
        result_df[column] = scaled_cumulative_sum.flatten()
    
    return result_df