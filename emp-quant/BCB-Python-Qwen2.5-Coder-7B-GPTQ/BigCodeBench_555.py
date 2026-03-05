import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
def task_func(a, b):
    """
    Calculate the Pearson correlation coefficient of two lists, generate a Pandas DataFrame from these lists,
    and then draw a scatter plot with a regression line.
    
    Parameters:
    a (list): The first list of numerical values.
    b (list): The second list of numerical values.
    
    Returns:
    tuple: Contains two elements:
        float: The Pearson correlation coefficient.
        matplotlib.axes.Axes: The Axes object of the plotted scatter plot with a regression line.
    """
    # Calculate the Pearson correlation coefficient
    correlation_coefficient = np.corrcoef(a, b)[0, 1]
    
    # Create a Pandas DataFrame from the lists
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Plot the scatter plot with a regression line
    fig, ax = plt.subplots()
    ax.scatter(df['A'], df['B'])
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['A'], df['B'])
    ax.plot(df['A'], slope * df['A'] + intercept, color='red')
    
    return correlation_coefficient, ax
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]