
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, cols):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")
    
    # Check if cols is a list
    if not isinstance(cols, list):
        raise ValueError("cols must be a list")
    
    # Check if all columns in cols exist in df
    if not all(col in df.columns for col in cols):
        raise ValueError("All columns in cols must exist in df")
    
    # Create a copy of the dataframe to avoid modifying the original
    df_copy = df.copy()
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the specified columns
    df_copy[cols] = scaler.fit_transform(df_copy[cols])
    
    return df_copy