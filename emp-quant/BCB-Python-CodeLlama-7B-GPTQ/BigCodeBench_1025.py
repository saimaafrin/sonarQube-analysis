import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
PLOT_TITLE = "Scaled Values"
def task_func(data_dict):
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
    "A": [1, 2, 3, 4, 5],
    "B": [6, 7, 8, 9, 10],
    "C": [11, 12, 13, 14, 15],
}