
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)

    # Create a MinMaxScaler object and fit it to the DataFrame
    scaler = MinMaxScaler()
    scaler.fit(df)

    # Scale the DataFrame using the scaler
    scaled_df = scaler.transform(df)

    # Create a matplotlib Axes object and plot the scaled data
    fig, ax = plt.subplots()
    ax.plot(scaled_df.index, scaled_df.values)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    plt.show()

    # Return the scaled DataFrame
    return scaled_df

scaled_df = task_func(data_dict)
print(scaled_df)