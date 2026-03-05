
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data, columns):
    """
    Normalizes specified columns of a DataFrame using min-max scaling.
    
    Parameters:
    - data (pd.DataFrame): The input DataFrame to be normalized.
    - columns (list): A list of column names to be normalized.
    
    Returns:
    - pd.DataFrame: A new DataFrame with the specified columns normalized between 0 and 1.
    """
    scaler = MinMaxScaler()
    data_copy = data.copy()
    data_copy[columns] = scaler.fit_transform(data_copy[columns])
    return data_copy