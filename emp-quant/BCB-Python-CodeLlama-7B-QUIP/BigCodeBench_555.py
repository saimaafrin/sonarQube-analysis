
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    corr_coef = stats.pearsonr(a, b)
    # Generate a Pandas DataFrame from the lists
    df = pd.DataFrame({'a': a, 'b': b})
    # Plot the scatter plot with a regression line
    ax = plt.scatter(df['a'], df['b'])
    ax.plot(df['a'], df['b'], 'r-')
    return corr_coef, ax