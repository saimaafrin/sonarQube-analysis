
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)

    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the data using the MinMaxScaler
    scaled_data = scaler.fit_transform(df)

    # Create a new DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

    # Plot the scaled data
    fig, ax = plt.subplots()
    ax.plot(scaled_df.index, scaled_df.values)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    return scaled_df, ax

scaled_df, ax = task_func(data_dict)

# Print the scaled data
print(scaled_df)

# Show the plot
plt.show()