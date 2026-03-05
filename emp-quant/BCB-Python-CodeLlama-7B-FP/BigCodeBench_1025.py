import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
PLOT_TITLE = "Scaled Values"
def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.

    Args:
        data_dict (dict): Dictionary containing the data to be scaled.

    Returns:
        pandas.DataFrame: Containing the scaled data.
        matplotlib.Axes: Object that displays the plot of the scaled data.
    """
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the data
    scaled_data = scaler.fit_transform(data_dict)

    # Create a pandas.DataFrame from the scaled data
    scaled_data_df = pd.DataFrame(scaled_data, columns=data_dict.keys())

    # Create a matplotlib.Axes object to plot the scaled data
    fig, ax = plt.subplots()

    # Plot the scaled data
    ax.plot(scaled_data_df)

    # Set the plot title
    ax.set_title(PLOT_TITLE)

    # Return the scaled data and the matplotlib.Axes object
    return scaled_data_df, ax
data_dict = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [6, 7, 8, 9, 10],
    "feature3": [11, 12, 13, 14, 15],
}