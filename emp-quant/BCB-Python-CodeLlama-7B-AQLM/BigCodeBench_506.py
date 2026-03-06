import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    """
    Analyze and visualize statistical properties of a specified weather data column.

    This function calculates the sum, mean, minimum, and maximum values of a specified column in the given data.
    It also generates a histogram plot of the data in the column. The dataset is expected to be a list of weather
    observations, where each observation includes date, temperature, humidity, wind speed, and precipitation values.
    If the provided data list is empty, resulting in an empty DataFrame, the function handles it by setting:
    - The 'mean' value to np.nan.
    - The 'min' value to np.inf.
    - The 'max' value to -np.inf.

    Parameters:
    column (str): The column to analyze. Valid columns include 'Temperature', 'Humidity', 'Wind Speed', and 'Precipitation'.
    data (list of lists): The weather data where each inner list contains the following format:
                          [Date (datetime object), Temperature (int), Humidity (int), Wind Speed (int), Precipitation (float)]

    Returns:
    - result (dict): A dictionary containing:
        - 'sum': Sum of the values in the specified column.
        - 'mean': Mean of the values in the specified column.
        - 'min': Minimum value in the specified column.
        - 'max': Maximum value in the specified column.
        - 'plot': A matplotlib BarContainer object of the histogram plot for the specified column.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot

    Example:
    >>> data = [[datetime(2022, 1, 1), -5, 80, 10, 0], [datetime(2022, 1, 3), -2, 83, 15, 0]]
    >>> result = task_func('Temperature', data)
    >>> result['sum']
    -7
    >>> type(result['plot'])
    <class 'matplotlib.container.BarContainer'>
    """
    # Check if the data list is empty
    if len(data) == 0:
        return {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf,
            'plot': None
        }

    # Convert the data list to a DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Temperature', 'Humidity', 'Wind Speed', 'Precipitation'])

    # Calculate the sum, mean, min, and max values of the specified column
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()

    # Generate a histogram plot of the specified column
    plot = df[column].hist(bins=10, color='#0072B2', edgecolor='#0072B2', linewidth=1.5, density=True)

    # Return the result
    return {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value,
        'plot': plot
    }