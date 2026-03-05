import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    """
    Normalize the last column of the DataFrame using MinMaxScaler from sklearn and plot the normalized data.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame with at least one column.
    
    Returns:
    pd.DataFrame: DataFrame with the last column normalized.
    Axes: Matplotlib Axes object representing the plot of the normalized last column.
    
    Raises:
    ValueError: If the input is not a DataFrame or if the DataFrame is empty.
    """
    # Check if the input is a DataFrame and is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Get the last column name
    last_column_name = df.columns[-1]
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the last column
    df[last_column_name] = scaler.fit_transform(df[[last_column_name]])
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    ax.plot(df.index, df[last_column_name], marker='o')
    ax.set_title(f'Normalized Data of {last_column_name}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    
    return df, ax