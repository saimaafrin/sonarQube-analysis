import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
def task_func(a, b):
    """
    Calculate the Pearson correlation coefficient of two lists, generate a Pandas DataFrame from these lists, and then draw a scatter plot with a regression line.
    The function should output with:
        tuple: Contains two elements:
        float: The Pearson correlation coefficient.
        matplotlib.axes.Axes: The Axes object of the plotted scatter plot with a regression line.
    """
    # Calculate the Pearson correlation coefficient
    corr_coef = stats.pearsonr(a, b)[0]

    # Generate a Pandas DataFrame from the lists
    df = pd.DataFrame({'a': a, 'b': b})

    # Draw a scatter plot with a regression line
    fig, ax = plt.subplots()
    ax.scatter(df['a'], df['b'])
    ax.plot(df['a'], df['b'], 'r--')
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_title('Scatter Plot with Regression Line')

    return corr_coef, ax
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]