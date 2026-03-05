
import pandas as pd
import seaborn as sns

def task_func(df):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if required columns are present
    required_columns = ['Date', 'Time', 'Temperature']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("DataFrame must contain 'Date', 'Time', and 'Temperature' columns")
    
    # Convert 'Date' and 'Time' columns to datetime
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    
    # Set 'DateTime' as the index
    df.set_index('DateTime', inplace=True)
    
    # Resample data to daily frequency and calculate mean temperature
    daily_temp = df['Temperature'].resample('D').mean()
    
    # Create a heatmap
    heatmap = sns.heatmap(daily_temp.unstack(), cmap='coolwarm')
    
    return heatmap