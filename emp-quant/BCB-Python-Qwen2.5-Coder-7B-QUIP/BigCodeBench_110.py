
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check if 'Date' and 'Sales' columns exist in the DataFrame
    if 'Date' not in df.columns or 'Sales' not in df.columns:
        raise ValueError("DataFrame must contain 'Date' and 'Sales' columns.")
    
    # Check if the DataFrame has data
    if df.empty:
        raise ValueError("DataFrame is empty.")
    
    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_title('Daily Turnover')
    
    return ax