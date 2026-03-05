
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string")
    if target_values is not None and not hasattr(target_values, '__iter__'):
        raise ValueError("target_values must be an array-like object")
    
    if target_values is not None:
        for col in df.columns:
            if col != target_column:
                df[col] = df[col].apply(lambda x: x if x in target_values else 0)
    
    model = LinearRegression()
    model.fit(df.drop(target_column, axis=1), df[target_column])
    
    return model