
import pandas as pd
import seaborn as sns
from scipy import stats
# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    # Check if the input data has exactly eight columns
    if data.shape[1] != 8:
        raise ValueError("Input data must have exactly eight columns.")
    
    # Calculate the average of each row
    data['Average'] = data.mean(axis=1)
    
    # Plot the distribution of the averages
    plot = sns.distplot(data['Average'], kde=True)
    
    # Perform the normality test
    if data.shape[0] >= 20:
        _, p_value = stats.normaltest(data['Average'])
    else:
        p_value = None
    
    return data, plot, p_value