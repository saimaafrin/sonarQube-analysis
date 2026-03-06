
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    correlation_coefficient = np.corrcoef(a, b)[0, 1]
    
    # Create a Pandas DataFrame
    data = {'A': a, 'B': b}
    df = pd.DataFrame(data)
    
    # Draw a scatter plot with a regression line
    fig, ax = plt.subplots()
    ax.scatter(df['A'], df['B'])
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['A'], df['B'])
    ax.plot(df['A'], slope * df['A'] + intercept, color='red')
    
    return (correlation_coefficient, ax)