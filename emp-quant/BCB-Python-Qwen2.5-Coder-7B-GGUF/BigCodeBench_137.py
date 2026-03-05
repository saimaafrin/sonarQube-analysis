
import pandas as pd
from scipy.stats import skew

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    last_column = df.columns[-1]
    return skew(df[last_column])