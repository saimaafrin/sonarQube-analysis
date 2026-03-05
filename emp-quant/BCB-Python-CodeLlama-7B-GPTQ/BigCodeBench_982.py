import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd
import numpy as np
def task_func(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    """
    Plots a histogram for a specified column of a pandas DataFrame and overlays it with a fitted normal distribution curve.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data to be plotted.
    column : str
        The name of the column in the DataFrame to be plotted.
    bins : int, optional
        The number of bins to use for the histogram. Default is 30.
    density : bool, optional
        Whether to normalize the histogram to have a density of 1. Default is True.
    alpha : float, optional
        The transparency of the normal distribution curve. Default is 0.6.
    color : str, optional
        The color of the normal distribution curve. Default is "g".
    seed : int, optional
        The random seed to use for the normal distribution curve. Default is None.

    Returns
    -------
    matplotlib.axes._axes.Axes
        The matplotlib Axes object with the plot.
    """
    # Generate the histogram
    hist, bins = np.histogram(df[column], bins=bins, density=density)

    # Generate the normal distribution curve
    mean = np.mean(df[column])
    std = np.std(df[column])
    x = np.linspace(bins[0], bins[-1], 100)
    y = norm.pdf(x, mean, std)

    # Plot the histogram and normal distribution curve
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0], alpha=alpha, color=color)
    ax.plot(x, y, color=color, label=f"Normal distribution curve (mean={mean:.2f}, std={std:.2f})")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.legend()

    return ax
data = np.random.normal(size=1000)
df = pd.DataFrame({"column": data})