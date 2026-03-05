import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if the required columns are present
    required_columns = ['Date', 'Time', 'Temperature']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {', '.join(missing_columns)}")
    
    # Convert 'Date' and 'Time' columns to datetime
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    
    # Set 'DateTime' as the index
    df.set_index('DateTime', inplace=True)
    
    # Resample the data to get daily average temperature
    df_daily = df.resample('D').mean()
    
    # Create a heatmap
    heatmap = sns.heatmap(df_daily['Temperature'].unstack(), cmap='coolwarm')
    
    # Set the title and labels
    heatmap.set_title('Daily Average Temperature')
    heatmap.set_xlabel('Date')
    heatmap.set_ylabel('Time')
    
    # Show the plot
    plt.show()
    
    # Return the heatmap object
    return heatmap