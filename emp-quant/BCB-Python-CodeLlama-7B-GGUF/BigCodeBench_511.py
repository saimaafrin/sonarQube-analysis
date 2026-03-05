
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Calculate statistics for the given column
    stats = data[column].describe()

    # Create a pie chart visualization of the data
    fig, ax = plt.subplots()
    ax.pie(data[column], labels=data[column], autopct='%1.1f%%')
    ax.set_title(f'Pie Chart of {column}')
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Value')

    return stats, ax