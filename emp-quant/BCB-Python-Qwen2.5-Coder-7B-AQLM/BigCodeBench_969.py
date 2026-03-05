
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        raise ValueError("The DataFrame is empty.")
    
    if df.isnull().values.any():
        raise ValueError("The DataFrame contains NaN values.")
    
    scaler = MinMaxScaler()
    
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    
    if not numeric_columns.empty:
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns].cumsum(axis=0))
    
    return df