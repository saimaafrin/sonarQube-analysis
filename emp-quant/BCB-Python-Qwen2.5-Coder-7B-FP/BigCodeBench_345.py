import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df, col1, col2):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("Input df is empty")
    
    # Check if the specified columns exist in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"Columns {col1} and {col2} must be in the DataFrame")
    
    # Check if the specified columns contain only numeric data
    if not (df[col1].dtype in ['int64', 'float64'] and df[col2].dtype in ['int64', 'float64']):
        raise TypeError("Columns must contain only numeric data")
    
    # Draw a scatter plot with a regression line
    axes = sns.lmplot(x=col1, y=col2, data=df)
    
    # Return the axes object
    return axes