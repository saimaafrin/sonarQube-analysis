import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(json_data: str, data_key: str):
    """
    Processes a JSON string to extract numerical data, Min-Max normalize them, and generate a line plot.

    Args:
        json_data (str): JSON string to process.
        data_key (str): Key path to the numerical data in the JSON string.

    Returns:
        Tuple:
            pd.Series: Original dataset in float64.
            pd.Series or None: Dataset after Min-Max scaling in float64, or None if data is empty.
            plt.Axes or None: Line plot of normalized data, or None if data is empty.

    Raises:
        KeyError: If key path is not found in the given data.
    """
    # Load JSON data
    data = json.loads(json_data)

    # Extract numerical data
    try:
        data_series = pd.Series(data[data_key])
    except KeyError:
        raise KeyError(f"Key path '{data_key}' not found in JSON data.")

    # Check if data is empty
    if data_series.empty:
        return data_series, None, None

    # Min-Max normalize data
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data_series.values.reshape(-1, 1))

    # Generate line plot
    fig, ax = plt.subplots()
    ax.plot(data_series.index, data_series.values, label="Original Data")
    ax.plot(data_series.index, normalized_data, label="Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.legend()

    return data_series, pd.Series(normalized_data), ax