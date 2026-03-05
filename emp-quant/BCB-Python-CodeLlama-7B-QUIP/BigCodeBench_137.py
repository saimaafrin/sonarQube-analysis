
import pandas as pd
from scipy.stats import skew

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.shape[1] == 0:
        raise ValueError("DataFrame has no columns")
    return skew(df.iloc[:, -1])