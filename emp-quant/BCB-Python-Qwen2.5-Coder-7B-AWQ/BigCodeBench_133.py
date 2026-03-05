import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    """
    Normalize the last column of the DataFrame using MinMaxScaler from sklearn and plot the normalized data.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame to be normalized.
    
    Returns:
    pd.DataFrame: A pandas DataFrame where the last column has been normalized.
    Axes: A Matplotlib Axes object representing the plot of the normalized last column.
    """
    # Check if the input is a DataFrame and is not empty
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    # Extract the last column
    last_column = df.iloc[:, -1]
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the last column
    normalized_column = scaler.fit_transform(last_column.values.reshape(-1, 1))
    
    # Replace the last column in the original DataFrame with the normalized values
    df.iloc[:, -1] = normalized_column
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    ax.plot(df.index, df.iloc[:, -1], label='Normalized Value')
    ax.set_title(f'Normalized Data of {df.columns[-1]}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    ax.legend()
    
    return df, ax