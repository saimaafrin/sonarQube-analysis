
import pandas as pd
from scipy.stats import skew

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if len(df.columns) == 0:
        raise ValueError("DataFrame has no columns")
    last_column = df.columns[-1]
    skewness = skew(df[last_column])
    return skewness