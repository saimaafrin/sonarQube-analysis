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
    
    # Initialize an empty list to store the normalized cumulative sums
    normalized_cumsums = []
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Check if the column is numeric
        if not np.issubdtype(df[column].dtype, np.number):
            raise TypeError(f"Column '{column}' contains non-numeric data types.")
        
        # Calculate the cumulative sum of the column
        cumsum = df[column].cumsum()
        
        # Reshape the cumulative sum to fit the MinMaxScaler
        cumsum_reshaped = cumsum.values.reshape(-1, 1)
        
        # Fit and transform the cumulative sum using MinMaxScaler
        normalized_cumsum = scaler.fit_transform(cumsum_reshaped)
        
        # Append the normalized cumulative sum to the list
        normalized_cumsums.append(normalized_cumsum)
    
    # Create a new DataFrame with the normalized cumulative sums
    normalized_df = pd.DataFrame(normalized_cumsums).T
    
    # Set the column names of the new DataFrame to the original column names
    normalized_df.columns = df.columns
    
    return normalized_df