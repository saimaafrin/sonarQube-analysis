
import bisect
import statistics
import numpy as np
import matplotlib.pyplot as plt

def task_func(df, column, value):
    if column not in df.columns:
        raise ValueError("Column does not exist in the DataFrame")
    if not isinstance(value, (int, float)):
        raise ValueError("Value is not a number")

    # Calculate the average of the column
    avg = df[column].mean()

    # Find the values greater than the average
    greater_than_avg = df[column][df[column] > avg]

    # Count the number of values greater than the given value
    count = len(greater_than_avg)

    # Create a histogram plot
    fig, ax = plt.subplots()
    ax.hist(greater_than_avg, bins=50)
    ax.set_title("Histogram of Values Greater Than Average")
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")

    return (greater_than_avg, count, ax)