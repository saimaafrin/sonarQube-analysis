import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    """
    Normalize the last column of the DataFrame using MinMaxScaler from sklearn and plot the normalized data.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame to be processed.
    
    Returns:
    pd.DataFrame: A pandas DataFrame where the last column has been normalized.
    Axes: A Matplotlib Axes object representing the plot of the normalized last column.
    
    Raises:
    ValueError: If the input is not a DataFrame or if the DataFrame is empty.
    """
    # Check if the input is a DataFrame and is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Get the name of the last column
    column_name = df.columns[-1]
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the last column
    df[column_name] = scaler.fit_transform(df[[column_name]])
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    ax.plot(df.index, df[column_name], label=column_name)
    ax.set_title(f'Normalized Data of {column_name}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    ax.legend()
    
    return df, ax