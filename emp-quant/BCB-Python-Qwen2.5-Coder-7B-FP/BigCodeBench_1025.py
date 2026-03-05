import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
PLOT_TITLE = "Scaled Values"
def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.
    
    Parameters:
    - data_dict: A dictionary where keys are column names and values are lists of data points.
    
    Returns:
    - scaled_df: A pandas DataFrame containing the scaled data.
    - ax: A matplotlib Axes object that displays the plot of the scaled data.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(data_dict)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a DataFrame from the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    
    # Plot the scaled data
    fig, ax = plt.subplots()
    scaled_df.plot(ax=ax)
    ax.set_title(PLOT_TITLE)
    
    return scaled_df, ax
data_dict = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [5, 4, 3, 2, 1]
}