import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    """
    Analyze a list of sales data, calculate the sum, the mean, the minimum, the maximum of a given column, and return the bar chart plot for the given column without displaying it.
    The function should raise the exception for: ValueError: If the quantity sold or total sales is negative.
    The function should output with:
        tuple: A tuple containing:
            dict: A dictionary with the sum, mean, min, max of the column.
            matplotlib.axes.Axes: The Axes object of the plotted bar chart. The bar chart will have Product in its
            x-axis and the title Bar Chart of (column).
    """
    # Check if the data is a valid pandas DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame")

    # Check if the column is a valid column in the DataFrame
    if column not in data.columns:
        raise ValueError("Column must be a valid column in the DataFrame")

    # Check if the data contains negative values
    if data[column].min() < 0:
        raise ValueError("Negative values are not allowed")

    # Calculate the sum, mean, minimum, and maximum of the column
    sum_ = data[column].sum()
    mean = data[column].mean()
    min_ = data[column].min()
    max_ = data[column].max()

    # Create a bar chart of the column
    fig, ax = plt.subplots()
    ax.bar(data["Product"], data[column])
    ax.set_title(f"Bar Chart of {column}")
    ax.set_xlabel("Product")
    ax.set_ylabel(column)

    # Return the tuple containing the dictionary and the Axes object
    return ({"sum": sum_, "mean": mean, "min": min_, "max": max_}, ax)
data = pd.DataFrame({"Product": ["A", "B", "C", "D", "E"], "Quantity": [10, 20, 30, 40, 50]})