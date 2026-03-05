import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
PLOT_TITLE = "Scaled Values"
def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.

    Args:
        data_dict (dict): A dictionary containing the data to be scaled.

    Returns:
        pandas.DataFrame: A pandas DataFrame containing the scaled data.
        matplotlib.Axes: A matplotlib Axes object that displays the plot of the scaled data.
    """
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the data
    scaled_data = scaler.fit_transform(data_dict)

    # Create a pandas DataFrame from the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=data_dict.keys())

    # Plot the scaled data
    fig, ax = plt.subplots()
    ax.plot(scaled_df)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    return scaled_df, ax
data_dict = {
    "a": [1, 2, 3, 4, 5],
    "b": [2, 4, 6, 8, 10],
    "c": [3, 6, 9, 12, 15]
}