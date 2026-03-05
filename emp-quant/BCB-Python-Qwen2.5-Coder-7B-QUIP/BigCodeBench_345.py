
import pandas as pd
import seaborn as sns

def task_func(df, col1, col2):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("Input df is empty")
    
    # Check if the specified columns exist in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"Input df does not contain the specified columns: {col1} and {col2}")
    
    # Check if the specified columns are numeric
    if not df[col1].dtype in ['int64', 'float64'] or not df[col2].dtype in ['int64', 'float64']:
        raise TypeError("Input df uses non-numeric data")
    
    # Draw a scatter plot with a regression line
    axes = sns.lmplot(x=col1, y=col2, data=df, scatter=True, line_rstyle='-', legend=False)
    
    return axes