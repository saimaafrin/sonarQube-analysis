
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(data_dict, data_keys):
    # Check if any of the keys in data_keys are present in data_dict
    if not any(key in data_dict for key in data_keys):
        raise ValueError("No keys in data_keys are found in data_dict")

    # Create a DataFrame from the data_dict
    df = pd.DataFrame(data_dict)

    # Create a MinMaxScaler object and fit it to the data
    scaler = MinMaxScaler()
    scaler.fit(df[data_keys])

    # Transform the data using the scaler
    scaled_data = scaler.transform(df[data_keys])

    # Create a new DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=data_keys)

    # Plot the scaled data
    fig, ax = plt.subplots()
    ax.plot(scaled_df.index, scaled_df.iloc[:, 0], label=data_keys[0])
    ax.plot(scaled_df.index, scaled_df.iloc[:, 1], label=data_keys[1])
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()

    return scaled_df, ax

scaled_df, ax = task_func(data_dict, data_keys)

print(scaled_df)