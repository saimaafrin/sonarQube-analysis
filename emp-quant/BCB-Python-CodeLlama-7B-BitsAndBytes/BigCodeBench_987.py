
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(json_data: str, data_key: str):
    # Load JSON data
    data = json.loads(json_data)

    # Extract numerical data from JSON
    data_series = pd.Series(data[data_key])

    # Check if data is empty
    if data_series.empty:
        return None, None, None

    # Min-Max normalize data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data_series.values.reshape(-1, 1))

    # Create line plot
    fig, ax = plt.subplots()
    ax.plot(data_series.index, data_series.values, label='Original Data')
    ax.plot(data_series.index, normalized_data, label='Normalized Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Comparison of Original and Normalized Data')
    ax.legend()

    return data_series, normalized_data, fig

original_data, normalized_data, fig = task_func(json_data, data_key)
print(original_data)
print(normalized_data)
print(fig)