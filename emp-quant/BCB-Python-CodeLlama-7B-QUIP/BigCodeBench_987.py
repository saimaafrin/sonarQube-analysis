
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(json_data: str, data_key: str):
    # Load JSON data
    data = json.loads(json_data)

    # Extract data from key path
    try:
        data = data[data_key]
    except KeyError:
        raise KeyError(f"Key {data_key} not found in JSON data")

    # Convert to pandas Series
    data = pd.Series(data)

    # Normalize data using Min-Max Scaler
    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(data)

    # Plot normalized data
    fig, ax = plt.subplots()
    ax.plot(data_normalized)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.legend()

    return data, data_normalized, fig