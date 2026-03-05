
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def task_func(a, b):
    # Calculate the Pearson correlation coefficient
    correlation_coefficient = stats.pearsonr(a, b)[0]
    
    # Create a Pandas DataFrame from the lists
    data = {'A': a, 'B': b}
    df = pd.DataFrame(data)
    
    # Draw a scatter plot with a regression line
    axes = df.plot(kind='scatter', x='A', y='B')
    slope, intercept, r_value, p_value, std_err = stats.linregress(a, b)
    axes.plot(a, slope * np.array(a) + intercept, color='red')
    
    return correlation_coefficient, axes