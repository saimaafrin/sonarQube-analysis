
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    
    if numeric_columns.empty:
        raise ValueError("DataFrame must contain at least one numeric column")
    
    axes = []
    for column in numeric_columns:
        ax = df[column].hist(bins=20, figsize=(8, 6))
        ax.set_title(column)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        axes.append(ax)
    
    return axes