
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the quantity sold or total sales is negative
    if any(data[column] < 0):
        raise ValueError("ValueError: Quantity sold or total sales cannot be negative")

    # Calculate the sum, mean, minimum, and maximum of the column
    sum_val = data[column].sum()
    mean_val = data[column].mean()
    min_val = data[column].min()
    max_val = data[column].max()

    # Create a bar chart plot of the column
    fig, ax = plt.subplots()
    ax.bar(data['Product'], data[column])
    ax.set_title(f"Bar Chart of {column}")
    ax.set_xlabel("Product")
    ax.set_ylabel(column)

    # Return the tuple containing the dictionary and the Axes object
    return ({
        'sum': sum_val,
        'mean': mean_val,
        'min': min_val,
        'max': max_val
    }, ax)

result = task_func('Quantity', data)
print(result)