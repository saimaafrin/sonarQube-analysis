import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
def task_func(df, dct, columns=None):
    """
    Preprocesses a pandas DataFrame by replacing specified values, encoding categorical attributes, and standardizing numerical attributes.
    
    Parameters:
    - df: pandas DataFrame to preprocess.
    - dct: Dictionary with keys as column names and values as dictionaries mapping old values to new values.
    - columns: List of columns to preprocess. If None, all columns are processed.
    
    Returns:
    - DataFrame: The preprocessed DataFrame with encoded categorical attributes and standardized numerical attributes.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    if columns is None:
        columns = df.columns
    
    for column in columns:
        if column in dct:
            # Replace specified values
            df[column] = df[column].replace(dct[column])
        
        if df[column].dtype == 'object':
            # Encode categorical attributes
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
        elif df[column].dtype in ['int64', 'float64']:
            # Standardize numerical attributes
            scaler = StandardScaler()
            df[column] = scaler.fit_transform(df[column].values.reshape(-1, 1))
    
    return df