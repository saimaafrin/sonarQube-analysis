
import pandas as pd
import seaborn as sns

def task_func(df):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if required columns exist
    required_columns = ['Date', 'Time', 'Temperature']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"DataFrame is missing the following columns: {', '.join(missing_columns)}")
    
    # Convert Date and Time to datetime format
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    
    # Set DateTime as the index
    df.set_index('DateTime', inplace=True)
    
    # Resample data to daily frequency and calculate mean temperature
    daily_temp = df.resample('D')['Temperature'].mean().reset_index()
    
    # Pivot table for plotting
    pivot_table = daily_temp.pivot(index='Date', columns=df.index.name, values='Temperature')
    
    # Create a heatmap
    axes = sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt=".1f", linewidths=.5)
    
    return axes