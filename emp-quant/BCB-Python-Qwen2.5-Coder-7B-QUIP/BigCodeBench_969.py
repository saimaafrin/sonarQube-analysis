
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Check if the DataFrame contains non-numeric data types
    if not df.select_dtypes(include=['number']).empty:
        raise TypeError("DataFrame contains non-numeric data types")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Apply the scaler to each column
    for column in df.columns:
        df[column] = scaler.fit_transform(df[column].values.reshape(-1, 1))
    
    return df