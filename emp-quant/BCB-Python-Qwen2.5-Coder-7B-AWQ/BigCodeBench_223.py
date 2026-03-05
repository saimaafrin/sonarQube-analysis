import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(df, dct, columns=None):
    """
    Preprocesses a pandas DataFrame by replacing specified values, encoding categorical attributes, and standardizing numerical attributes.
    
    Parameters:
    - df: pandas DataFrame to be preprocessed.
    - dct: Dictionary containing the mapping for value replacement.
    - columns: List of column names to be processed. If None, all columns are processed.
    
    Returns:
    - DataFrame: The preprocessed DataFrame with encoded categorical attributes and standardized numerical attributes.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    if columns is None:
        columns = df.columns
    
    for col in columns:
        if col in dct:
            df[col] = df[col].replace(dct[col])
        
        if df[col].dtype == 'object':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
        else:
            mean = df[col].mean()
            std = df[col].std()
            df[col] = (df[col] - mean) / std
    
    return df