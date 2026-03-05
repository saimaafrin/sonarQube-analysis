import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")
    
    # Check for required columns
    required_columns = ['Date', 'Time', 'Temperature']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
    # Convert 'Date' and 'Time' columns to datetime and time objects respectively
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time
    
    # Pivot the DataFrame to have 'Date' as index, 'Time' as columns, and 'Temperature' as values
    pivot_df = df.pivot(index='Date', columns='Time', values='Temperature')
    
    # Create a heatmap using seaborn
    heatmap = sns.heatmap(pivot_df, cmap='YlGnBu', annot=True, fmt=".1f")
    
    # Set the title and labels
    heatmap.set_title('Temperature Heatmap')
    heatmap.set_xlabel('Time')
    heatmap.set_ylabel('Date')
    
    # Show the plot
    plt.show()
    
    # Return the heatmap object
    return heatmap