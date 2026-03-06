
import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(json_data: str, data_key: str):
    try:
        # Load JSON data
        data = json.loads(json_data)
        
        # Extract the data using the provided key path
        values = data.get(data_key)
        if values is None:
            raise KeyError(f"The key '{data_key}' was not found in the provided JSON data.")
        
        # Convert the extracted data into a pandas Series
        original_series = pd.Series(values, dtype=float)
        
        # Check if the series is empty
        if original_series.empty:
            return original_series, None, None
        
        # Initialize the Min-Max scaler
        scaler = MinMaxScaler()
        
        # Fit and transform the data
        normalized_values = scaler.fit_transform(original_series.values.reshape(-1, 1))
        
        # Create a pandas Series for the normalized data
        normalized_series = pd.Series(normalized_values.flatten(), index=original_series.index, name='Normalized Data')
        
        # Plotting
        fig, ax = plt.subplots()
        ax.plot(original_series, label="Original Data")
        ax.plot(normalized_series, label="Normalized Data")
        ax.set_title("Comparison of Original and Normalized Data")
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.legend()
        
        return original_series, normalized_series, ax
    
    except KeyError as e:
        print(e)
        return None, None, None