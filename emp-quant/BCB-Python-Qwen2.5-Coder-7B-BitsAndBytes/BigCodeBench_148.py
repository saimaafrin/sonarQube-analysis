
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encrypts the categorical data in a specific column of a DataFrame using LabelEncoder.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing categorical data.
    column_name (str): The name of the column to be encoded.

    Returns:
    pd.DataFrame: The DataFrame with the encoded column.
    """
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()
    
    # Fit and transform the specified column
    df[column_name] = label_encoder.fit_transform(df[column_name])
    
    return df