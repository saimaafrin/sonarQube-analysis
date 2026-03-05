
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if required columns are present
    required_columns = ['Date', 'Time', 'Temperature']
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"DataFrame must contain the column: {column}")
    
    # Convert 'Date' and 'Time' columns to datetime
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    
    # Set 'DateTime' as the index
    df.set_index('DateTime', inplace=True)
    
    # Resample data to daily frequency and calculate mean temperature
    daily_temp = df['Temperature'].resample('D').mean()
    
    # Create a heatmap
    heatmap = sns.heatmap(daily_temp.unstack(), cmap='YlGnBu')
    
    # Set labels and title
    heatmap.set_xlabel('Time')
    heatmap.set_ylabel('Date')
    heatmap.set_title('Daily Temperature Heatmap')
    
    # Show the plot
    plt.show()
    
    return heatmap