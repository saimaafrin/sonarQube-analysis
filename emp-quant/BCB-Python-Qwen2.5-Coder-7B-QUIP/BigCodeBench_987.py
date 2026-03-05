
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(json_data: str, data_key: str):
    # Load JSON data
    data = json.loads(json_data)
    
    # Extract the data using the key
    try:
        data_values = data[data_key]
    except KeyError:
        raise KeyError(f"Key '{data_key}' not found in the data.")
    
    # Convert the data to a pandas Series
    original_data = pd.Series(data_values, name='Original Data')
    
    # Check if the data is empty
    if original_data.empty:
        normalized_data = None
        plot_ax = None
    else:
        # Min-Max normalization
        scaler = MinMaxScaler()
        normalized_data = scaler.fit_transform(original_data.values.reshape(-1, 1))
        normalized_data = pd.Series(normalized_data[:, 0], name='Normalized Data')
        
        # Plot the data
        fig, ax = plt.subplots()
        ax.plot(original_data.index, original_data, label='Original Data')
        ax.plot(normalized_data.index, normalized_data, label='Normalized Data')
        ax.set_title('Comparison of Original and Normalized Data')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.legend()
        
        plot_ax = ax
    
    return original_data, normalized_data, plot_ax