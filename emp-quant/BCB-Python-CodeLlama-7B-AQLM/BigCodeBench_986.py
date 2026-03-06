import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def task_func(json_data: str, key_path: list):
    """
    Extracts and visualizes numerical data from a JSON structure based on a specified path of keys.

    Parameters:
    json_data (str): JSON formatted string.
    key_path (list): List of strings representing the nested keys to locate the data within the JSON.

    Returns:
    matplotlib.figure.Figure: A matplotlib figure showing a boxplot of the data values.

    Raises:
    KeyError: If a specified key is not found.
    ValueError: If no numeric data is found, or the data string is empty or corrupted.

    Requirements:
    - json
    - numpy
    - matplotlib
    - seaborn
    - pandas

    Examples:
    >>> json_data = '{"level1":{"level2":{"data":"1,2,3,4"}}}'
    >>> key_path = ['level1', 'level2', 'data']
    >>> fig = task_func(json_data, key_path)
    >>> isinstance(fig, plt.Figure)
    True
    """
    # Load JSON data
    data = json.loads(json_data)

    # Extract data
    try:
        data = data
        for key in key_path:
            data = data[key]
    except KeyError:
        raise KeyError('Key not found.')

    # Check if data is numeric
    try:
        data = np.array(data.split(','), dtype=float)
    except ValueError:
        raise ValueError('No numeric data found.')

    # Check if data is empty
    if len(data) == 0:
        raise ValueError('No data found.')

    # Visualize data
    fig = plt.figure()
    sns.boxplot(data=pd.DataFrame(data))
    plt.show()

    return fig