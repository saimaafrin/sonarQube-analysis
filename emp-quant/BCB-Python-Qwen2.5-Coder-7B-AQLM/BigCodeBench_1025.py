
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.
    
    Parameters:
    data_dict (dict): A dictionary where keys are column names and values are lists of data points.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the scaled data.
    matplotlib.Axes: An Axes object that displays the plot of the scaled data.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(data_dict)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a DataFrame with scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    
    # Plot the scaled data
    fig, ax = plt.subplots()
    scaled_df.plot(kind='bar', ax=ax)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel('Features')
    ax.set_ylabel('Scaled Values')
    
    return scaled_df, ax