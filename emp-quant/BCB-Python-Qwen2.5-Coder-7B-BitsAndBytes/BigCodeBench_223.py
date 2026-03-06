
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(df, dct, columns=None):
    """
    Preprocesses a pandas DataFrame by replacing specified values, encoding categorical attributes,
    and standardizing numerical attributes.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to preprocess.
    - dct (dict): A dictionary mapping column names to their corresponding replacements.
    - columns (list, optional): List of columns to apply preprocessing on. If None, all columns are processed.

    Returns:
    - pd.DataFrame: The preprocessed DataFrame with encoded categorical attributes and standardized numerical attributes.
    """
    
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a pandas DataFrame.")
    
    # Apply value replacements
    if columns is None:
        columns = df.columns
    
    for col in columns:
        if col in dct:
            df[col] = df[col].replace(dct[col])
    
    # Encode categorical attributes
    le = LabelEncoder()
    for col in columns:
        if df[col].dtype == 'object':
            df[col] = le.fit_transform(df[col])
    
    # Standardize numerical attributes
    for col in columns:
        if df[col].dtype in ['int64', 'float64']:
            mean = df[col].mean()
            std = df[col].std()
            df[col] = (df[col] - mean) / std
    
    return df