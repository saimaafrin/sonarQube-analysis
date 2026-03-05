
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_dict, data_keys):
    # Check if the keys are present in the data dictionary
    if not all(key in data_dict for key in data_keys):
        raise ValueError("No keys in `data_keys` are found in `data_dict`")

    # Create a DataFrame from the data dictionary
    data = pd.DataFrame(data_dict)

    # Normalize the data using the MinMaxScaler
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data[data_keys])

    # Create a new DataFrame with the normalized data
    normalized_data_df = pd.DataFrame(normalized_data, columns=data_keys)

    # Plot the normalized data
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(normalized_data_df)
    ax.set_xlabel("Normalized data")
    ax.set_ylabel("Value")
    ax.set_title("Normalized data")
    plt.show()

    return normalized_data_df, fig