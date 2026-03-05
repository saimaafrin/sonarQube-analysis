import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the DataFrame contains NaN values
    if df.isnull().any().any():
        raise ValueError("The DataFrame contains NaN values.")
    
    # Initialize a list to store the normalized cumulative sums
    normalized_cumsums = []
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Check if the column is numeric
        if pd.api.types.is_numeric_dtype(df[column]):
            # Calculate the cumulative sum
            cumsum = df[column].cumsum()
            # Initialize the MinMaxScaler
            scaler = MinMaxScaler()
            # Reshape the cumulative sum to fit the scaler
            cumsum_reshaped = cumsum.values.reshape(-1, 1)
            # Fit and transform the cumulative sum
            normalized_cumsum = scaler.fit_transform(cumsum_reshaped)
            # Append the normalized cumulative sum to the list
            normalized_cumsums.append(normalized_cumsum.flatten())
        else:
            # Raise TypeError if the column is not numeric
            raise TypeError(f"Column '{column}' contains non-numeric data types.")
    
    # Create a new DataFrame with the normalized cumulative sums
    result_df = pd.DataFrame(normalized_cumsums).T
    # Set the column names of the result DataFrame to the original column names
    result_df.columns = df.columns
    
    return result_df