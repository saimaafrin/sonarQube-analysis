import json
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(json_data: str, data_key: str):
    """
    Processes a JSON string to extract numerical data, Min-Max normalize them, and generate a line plot.

    Parameters
    ----------
    json_data : str
        JSON string to be processed.
    data_key : str
        Key path to the numerical data in the JSON string.

    Returns
    -------
    pd.Series
        Original dataset in float64.
    pd.Series or None
        Dataset after Min-Max scaling in float64, or None if data is empty.
    plt.Axes or None
        Line plot of normalized data, or None if data is empty.

    Raises
    ------
    KeyError
        If key path is not found in the given data.
    """
    # Load JSON data
    data = json.loads(json_data)

    # Extract numerical data
    try:
        data = data[data_key]
    except KeyError:
        raise KeyError(f"Key path {data_key} not found in JSON data.")

    # Convert data to float64
    data = data.astype(float)

    # Min-Max scale data
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    # Generate line plot
    fig, ax = plt.subplots()
    ax.plot(data, label="Original Data")
    ax.plot(data_scaled, label="Normalized Data")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title("Comparison of Original and Normalized Data")
    ax.legend()

    return data, data_scaled, ax
data = ""
data_key = "data"