
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    corr_coef = stats.pearsonr(a, b)[0]

    # Create a Pandas DataFrame from the lists
    df = pd.DataFrame({'a': a, 'b': b})

    # Draw a scatter plot with a regression line
    fig, ax = plt.subplots()
    ax.scatter(df['a'], df['b'])
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_title('Scatter Plot with Regression Line')
    ax.plot(df['a'], df['b'], 'r')
    plt.show()

    return corr_coef, ax