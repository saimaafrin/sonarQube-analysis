
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Validate the column name
    if column not in data.columns:
        raise KeyError("Invalid column name")

    # Validate the data list
    if len(data) == 0:
        raise ValueError("Data list is empty")
    for i in range(len(data)):
        if data[i][column] < 0:
            raise ValueError("Negative value found in column " + column)

    # Calculate the sum, mean, min, and max of the column
    sum = data[column].sum()
    mean = data[column].mean()
    min = data[column].min()
    max = data[column].max()

    # Plot the line chart
    fig, ax = plt.subplots()
    ax.plot(data[column])
    ax.set_xlabel("Date")
    ax.set_ylabel(column)
    ax.set_title("Line Chart of " + column)

    return (sum, mean, min, max, ax)