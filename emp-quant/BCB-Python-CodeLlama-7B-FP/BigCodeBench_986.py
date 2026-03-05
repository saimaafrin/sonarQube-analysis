import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def task_func(json_data: str, key_path: list):
    """
    Extracts and visualizes numerical data from a JSON structure based on a specified path of keys.
    Raises:
        KeyError: If a specified key is not found.
        ValueError: If no numeric data is found, or the data string is empty or corrupted.
    Returns:
        matplotlib.figure.Figure: A matplotlib figure showing a boxplot of the data values.
    """
    # Load the JSON data
    data = json.loads(json_data)

    # Extract the data from the JSON structure
    try:
        data_values = [data[key] for key in key_path]
    except KeyError:
        raise KeyError(f"Key {key_path[-1]} not found in JSON data")

    # Check if the data is numeric
    if not all(isinstance(value, (int, float)) for value in data_values):
        raise ValueError("Non-numeric data found in JSON data")

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data_values)

    # Create a boxplot of the data
    fig, ax = plt.subplots()
    sns.boxplot(data=df, ax=ax)

    # Return the matplotlib figure
    return fig
json_data = '{"a": {"b": {"c": 1}, "d": {"e": 2}}, "f": {"g": 3}}'
key_path = ["a", "b", "c"]