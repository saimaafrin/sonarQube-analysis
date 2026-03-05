import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df, cols):
    # Check if 'df' is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'cols' is a list
    if not isinstance(cols, list):
        raise ValueError("Input 'cols' must be a list of column names.")
    
    # Check if all columns in 'cols' exist in 'df'
    if not all(col in df.columns for col in cols):
        raise ValueError("All columns in 'cols' must exist in the DataFrame 'df'.")
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Standardize the specified columns
    df[cols] = scaler.fit_transform(df[cols])
    
    return df