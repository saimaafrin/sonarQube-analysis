
import pandas as pd
from scipy.stats import skew

def task_func(df):
    if not isinstance(df, pd.DataFrame) or not df.columns:
        raise ValueError("Input must be a DataFrame with at least one column.")
    
    last_column = df.iloc[:, -1]
    return float(skew(last_column))