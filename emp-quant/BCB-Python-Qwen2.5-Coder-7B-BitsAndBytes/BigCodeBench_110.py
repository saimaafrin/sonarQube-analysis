
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if 'Date' and 'Sales' columns exist
    required_columns = ['Date', 'Sales']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"DataFrame must contain the following columns: {', '.join(required_columns)}. Missing columns: {', '.join(missing_columns)}")
    
    # Check if there is any data to plot
    if df.empty:
        raise ValueError("DataFrame contains no data to plot.")
    
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set 'Date' column as the index
    df.set_index('Date', inplace=True)
    
    # Plot the line chart
    axes = df['Sales'].plot(kind='line')
    
    return axes