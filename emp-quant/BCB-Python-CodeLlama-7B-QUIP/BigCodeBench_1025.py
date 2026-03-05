
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    # Initialize the scaler
    scaler = MinMaxScaler()

    # Scale the data
    scaled_data = scaler.fit_transform(data_dict)

    # Create a pandas DataFrame from the scaled data
    scaled_df = pd.DataFrame(scaled_data)

    # Plot the scaled data
    fig, ax = plt.subplots()
    ax.plot(scaled_df)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.set_zlabel("Feature 3")

    return scaled_df, fig