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
    - pd.DataFrame: DataFrame with the 'Date' column and additional columns for each element in the original 'Value' list.
    - Axes (optional): A matplotlib Axes object containing the bar chart, returned if 'plot' is True.
    """
    # Check if the DataFrame has the required columns
    if not all(col in df.columns for col in COLUMNS):
        raise KeyError("DataFrame must contain 'Date' and 'Value' columns.")
    
    # Convert 'Date' column to datetime and set as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Split 'Value' column into multiple columns
    value_columns = df['Value'].apply(pd.Series)
    
    # Scale the value columns
    scaler = StandardScaler()
    scaled_value_columns = scaler.fit_transform(value_columns)
    scaled_value_columns = pd.DataFrame(scaled_value_columns, columns=value_columns.columns, index=value_columns.index)
    
    # Combine the scaled value columns with the 'Date' column
    result_df = pd.concat([df['Date'], scaled_value_columns], axis=1)
    
    # Plot the scaled values over time if plot is True
    if plot:
        fig, ax = plt.subplots()
        for column in scaled_value_columns.columns:
            ax.bar(result_df.index, scaled_value_columns[column], label=column)
        ax.set_title('Scaled Values Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Scaled Value')
        ax.legend()
        return result_df, ax
    else:
        return result_df