
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    scaler = MinMaxScaler()
    
    # Check if all columns are numeric
    if not np.issubdtype(df.values.dtype, np.number):
        raise TypeError("DataFrame contains non-numeric data types")
    
    # Replace NaN values with 0 to avoid errors during scaling
    df_filled = df.fillna(0)
    
    # Apply MinMaxScaler to each column and compute cumulative sum
    scaled_cumsum_df = pd.DataFrame(scaler.fit_transform(df_filled.cumsum()), columns=df.columns)
    
    return scaled_cumsum_df