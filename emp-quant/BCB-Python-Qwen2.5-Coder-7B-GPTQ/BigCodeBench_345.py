import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df, col1, col2):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Check if the specified columns exist in the DataFrame
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"Columns {col1} and {col2} must exist in the DataFrame")
    
    # Check if the specified columns contain numeric data
    if not pd.api.types.is_numeric_dtype(df[col1]) or not pd.api.types.is_numeric_dtype(df[col2]):
        raise TypeError(f"Columns {col1} and {col2} must contain numeric data")
    
    # Draw a scatter plot with a regression line
    axes = sns.regplot(x=col1, y=col2, data=df)
    
    # Show the plot
    plt.show()
    
    return axes