import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    corr_coef = stats.pearsonr(a, b)[0]

    # Generate a Pandas DataFrame from the lists
    df = pd.DataFrame({'a': a, 'b': b})

    # Draw a scatter plot with a regression line
    fig, ax = plt.subplots()
    ax.scatter(df['a'], df['b'])
    ax.plot(df['a'], df['b'].rolling(window=10).mean())
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_title('Scatter Plot with Regression Line')

    # Return the Pearson correlation coefficient and the Axes object
    return (corr_coef, ax)
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]