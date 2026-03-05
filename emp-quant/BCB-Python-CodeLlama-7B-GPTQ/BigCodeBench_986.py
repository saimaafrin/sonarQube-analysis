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
        data_values = [data[key_path[0]] for key_path in key_path[1:]]
    except KeyError:
        raise KeyError("Key not found in JSON data")

    # Convert the data to a list of numbers
    data_values = [float(value) for value in data_values]

    # Check if the data is empty or corrupted
    if not data_values:
        raise ValueError("No numeric data found")

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data_values, columns=["data"])

    # Create a boxplot of the data
    fig, ax = plt.subplots()
    sns.boxplot(data=df, orient="v", ax=ax)

    # Return the matplotlib figure
    return fig
json_data = '{"key1": {"key2": {"key3": 10}}, "key4": {"key5": 20}}'
key_path = ["key1", "key2", "key3"]