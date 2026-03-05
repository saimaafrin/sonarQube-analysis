import pandas as pd
from scipy.stats import skew
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    
    # Check if the DataFrame has columns
    if df.empty or df.columns.empty:
        raise ValueError("DataFrame must have at least one column")
    
    # Calculate the skewness of the last column
    last_column_skewness = skew(df.iloc[:, -1])
    
    return last_column_skewness