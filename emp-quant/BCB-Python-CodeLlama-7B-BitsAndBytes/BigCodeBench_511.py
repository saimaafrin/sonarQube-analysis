
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Calculate statistics for the given column
    stats = {
        'sum': data[column].sum(),
        'mean': data[column].mean(),
        'min': data[column].min(),
        'max': data[column].max()
    }

    # Create a pie chart visualization of the data
    labels = data[column].values
    sizes = data[column].value_counts()
    explode = (0.1, 0.1)
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    return stats, ax