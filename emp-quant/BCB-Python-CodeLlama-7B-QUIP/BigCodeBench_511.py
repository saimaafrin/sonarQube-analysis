
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Calculate statistics for the given column
    stats = {
        'sum': data[column].sum(),
        'mean': data[column].mean(),
        'min': data[column].min(),
        'max': data[column].max(),
    }

    # Visualize the data with a pie chart
    fig, ax = plt.subplots()
    ax.pie(data[column], labels=data[column])
    ax.set_title(f"Pie chart of {column}")
    plt.show()

    return stats, fig