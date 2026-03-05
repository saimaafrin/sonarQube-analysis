
import pandas as pd
from scipy.stats import skew

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    if df.columns.empty:
        raise ValueError("DataFrame must have at least one column")
    
    last_column = df.iloc[:, -1]
    return skew(last_column)