
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    correlation_coefficient = stats.pearsonr(a, b)[0]
    
    # Create a Pandas DataFrame from the lists
    df = pd.DataFrame({'x': a, 'y': b})
    
    # Draw a scatter plot with a regression line
    fig, ax = plt.subplots()
    ax.scatter(df['x'], df['y'], color='blue')
    ax.plot(df['x'], df['y'], 'r-', label='Regression Line')
    
    # Return the correlation coefficient and the Axes object
    return correlation_coefficient, ax