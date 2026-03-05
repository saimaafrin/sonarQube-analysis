
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if 'Date' and 'Sales' columns exist
    if 'Date' not in df.columns or 'Sales' not in df.columns:
        raise ValueError("DataFrame must contain 'Date' and 'Sales' columns")
    
    # Check if there is any data to plot
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set 'Date' column as the index
    df.set_index('Date', inplace=True)
    
    # Create the line chart
    fig, ax = plt.subplots()
    ax.plot(df.index, df['Sales'], marker='o')
    
    # Set the title and labels
    ax.set_title('Daily Turnover')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    
    # Return the Axes object
    return ax