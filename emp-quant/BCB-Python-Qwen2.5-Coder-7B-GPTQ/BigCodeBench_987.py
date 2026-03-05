import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(json_data: str, data_key: str):
    # Load JSON data
    data = json.loads(json_data)
    
    # Extract the data using the provided key
    try:
        values = data[data_key]
    except KeyError:
        raise KeyError(f"Key '{data_key}' not found in the provided JSON data.")
    
    # Convert the data to a pandas Series
    original_data = pd.Series(values, dtype=float)
    
    # Check if the data is empty
    if original_data.empty:
        return original_data, None, None
    
    # Min-Max normalize the data
    scaler = MinMaxScaler()
    normalized_data = pd.Series(scaler.fit_transform(original_data.values.reshape(-1, 1)).flatten(), dtype=float)
    
    # Create a line plot
    fig, ax = plt.subplots()
    ax.plot(original_data.index, original_data, label="Original Data")
    ax.plot(normalized_data.index, normalized_data, label="Normalized Data")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()
    
    return original_data, normalized_data, ax