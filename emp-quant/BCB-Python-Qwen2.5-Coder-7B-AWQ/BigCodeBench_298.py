import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
COLUMNS = ['Date', 'Value']
def task_func(df, plot=False):
    """
    Splits a list in the 'Value' column of a DataFrame into several columns, scales these columns using StandardScaler,
    and optionally returns the scaled data using a bar chart. The 'Date' column is converted to datetime and used as the index
    in the plot.
    
    Parameters:
    - df (pd.DataFrame): Input DataFrame with 'Date' and 'Value' columns.
    - plot (bool): If True, returns a matplotlib Axes object containing the bar chart.
    
    Returns:
    - pd.DataFrame: A pandas DataFrame with the 'Date' column and additional columns for each element in the original 'Value' list,
      where these columns contain the scaled values.
    - Axes (optional): A matplotlib Axes object containing the bar chart, returned if 'plot' is True.
    """
    # Check if 'Date' and 'Value' columns exist
    if not all(col in df.columns for col in COLUMNS):
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns.")
    
    # Convert 'Date' column to datetime and set as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Split 'Value' column into multiple columns
    df_expanded = pd.DataFrame(df['Value'].tolist(), index=df.index)
    
    # Scale the expanded DataFrame
    scaler = StandardScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df_expanded), columns=df_expanded.columns, index=df_expanded.index)
    
    # Optionally plot the scaled data
    if plot:
        ax = scaled_df.plot(kind='bar', figsize=(10, 6))
        ax.set_title('Scaled Values Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Scaled Value')
        return scaled_df, ax
    
    return scaled_df