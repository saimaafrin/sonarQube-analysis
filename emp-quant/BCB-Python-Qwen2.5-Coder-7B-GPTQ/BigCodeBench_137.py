import pandas as pd
from scipy.stats import skew
def task_func(df):
    # Check if the input is a DataFrame and has columns
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    # Calculate the skewness of the last column
    last_column_skewness = skew(df.iloc[:, -1])
    
    return last_column_skewness