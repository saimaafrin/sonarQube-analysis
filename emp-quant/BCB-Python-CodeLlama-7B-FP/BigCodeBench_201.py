import bisect
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(df, column, value):
    """
    Analyze a column of a pandas DataFrame, find the values that are larger than the average, and count the number of values that are larger than a given value.
    The function should raise the exception for: ValueError: If the column does not exist in the DataFrame or value is not a number.
    The function should output with:
        tuple: A tuple containing (numpy.ndarray, int, matplotlib.axes.Axes).
        The numpy array contains values greater than the average.
        The int is the number of values greater than the given value.
        The Axes object is for the generated histogram plot.
    """
    if column not in df.columns:
        raise ValueError(f"Column {column} does not exist in the DataFrame")
    if not isinstance(value, (int, float)):
        raise ValueError(f"Value {value} is not a number")

    # Calculate the average of the column
    average = df[column].mean()

    # Find the values in the column that are greater than the average
    greater_than_average = df[column][df[column] > average]

    # Count the number of values greater than the given value
    count = greater_than_average.count()

    # Generate a histogram plot of the values
    fig, ax = plt.subplots()
    ax.hist(greater_than_average, bins=50)
    ax.set_title(f"Histogram of values in {column} greater than {value}")
    ax.set_xlabel(f"Value in {column}")
    ax.set_ylabel("Count")

    return greater_than_average, count, ax
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})