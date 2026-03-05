import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if 'Date' and 'Sales' columns exist in the DataFrame
    required_columns = ['Date', 'Sales']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("DataFrame must contain 'Date' and 'Sales' columns")
    
    # Check if there is any data to plot
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set 'Date' column as the index
    df.set_index('Date', inplace=True)
    
    # Plot the line chart
    axes = df['Sales'].plot(kind='line', figsize=(10, 5))
    
    # Return the Axes object
    return axes