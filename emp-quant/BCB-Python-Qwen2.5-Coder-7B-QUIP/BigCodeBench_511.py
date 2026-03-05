
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data list is empty
    if not data:
        return {}, {}, None

    # Convert the data list to a pandas Series
    series = pd.Series(data, name=column)

    # Calculate the sum, mean, min, and max of the column
    sum_value = series.sum()
    mean_value = series.mean()
    min_value = series.min()
    max_value = series.max()

    # Create a dictionary with the calculated statistics
    stats = {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value
    }

    # Create a pie chart using the Age column as labels
    fig, ax = plt.subplots()
    ax.pie(series.value_counts(), labels=series.value_counts().index, autopct='%1.1f%%')
    ax.set_title(f'Pie Chart of {column}')

    # Return the statistics and the pie chart
    return stats, stats, ax