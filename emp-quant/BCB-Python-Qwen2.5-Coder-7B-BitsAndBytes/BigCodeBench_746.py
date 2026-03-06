
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target_column, target_values=None):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")
    
    # Check if target_column is a string
    if not isinstance(target_column, str):
        raise ValueError("target_column must be a string")
    
    # Check if target_values is an array-like object
    if target_values is not None and not hasattr(target_values, '__iter__'):
        raise ValueError("target_values must be an array-like object")
    
    # Replace elements not in target_values with zero
    if target_values is not None:
        for col in df.columns:
            if col != target_column:
                df[col] = df[col].apply(lambda x: x if x in target_values else 0)
    
    # Initialize and fit the Linear Regression model
    model = LinearRegression()
    model.fit(df.drop(columns=[target_column]), df[target_column])
    
    return model