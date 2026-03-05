import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd
import numpy as np
def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    """
    Plots a histogram for a specified column of a pandas DataFrame and overlays it with a fitted normal distribution curve.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    column (str): The name of the column to plot.
    bins (int, optional): The number of bins to use for the histogram. Defaults to 30.
    density (bool, optional): Whether to normalize the histogram to have a total area of 1. Defaults to True.
    alpha (float, optional): The transparency of the histogram. Defaults to 0.6.
    color (str, optional): The color of the histogram. Defaults to "g".
    seed (int, optional): The random seed to use for the histogram. Defaults to None.

    Returns:
    matplotlib.axes._axes.Axes: The matplotlib Axes object with the plot.
    """
    # Generate the histogram
    hist, bins = np.histogram(df[column], bins=bins, density=density)

    # Generate the normal distribution curve
    mean = df[column].mean()
    std = df[column].std()
    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    y = norm.pdf(x, mean, std)

    # Plot the histogram and the normal distribution curve
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, alpha=alpha, color=color)
    ax.plot(x, y, label="Normal distribution")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of {}".format(column))
    ax.legend()

    return ax
data = pd.DataFrame({"A": np.random.normal(0, 1, 100)})