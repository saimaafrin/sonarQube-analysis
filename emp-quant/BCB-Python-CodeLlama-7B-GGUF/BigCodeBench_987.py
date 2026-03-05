
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(json_data: str, data_key: str):
    # Load JSON data
    data = json.loads(json_data)

    # Extract numerical data from JSON
    try:
        data_series = pd.Series(data[data_key])
    except KeyError:
        raise KeyError(f"Key path {data_key} not found in JSON data")

    # Min-Max normalize data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data_series.values.reshape(-1, 1))

    # Create line plot
    fig, ax = plt.subplots()
    ax.plot(data_series.index, data_series.values, label="Original Data")
    ax.plot(normalized_data[:, 0], normalized_data[:, 1], label="Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.legend()

    return data_series, normalized_data, ax