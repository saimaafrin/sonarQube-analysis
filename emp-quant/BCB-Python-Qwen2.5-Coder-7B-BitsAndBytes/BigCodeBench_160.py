
import pandas as pd
import seaborn as sns
from scipy import stats

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    """
    Processes a given dataset to compute the average of each row,
    plots the distribution of these averages, and evaluates their normality.

    Parameters:
    - data (pd.DataFrame): Input DataFrame with exactly 8 columns.

    Returns:
    - tuple: Contains three elements:
        - DataFrame: Original DataFrame with an added 'Average' column.
        - Axes object: Seaborn distribution plot of the averages.
        - float or None: P-value from the normality test, or None if not applicable.
    """
    # Check if the input data has exactly 8 columns
    if data.shape[1] != len(COLUMN_NAMES):
        raise ValueError("Input data must have exactly 8 columns.")

    # Compute the average of each row
    data['Average'] = data.mean(axis=1)

    # Plot the distribution of the averages
    plot = sns.distplot(data['Average'], kde=True)
    
    # Evaluate normality if there are at least 20 data points
    p_value = None
    if len(data) >= 20:
        _, p_value = stats.normaltest(data['Average'])
    
    return data, plot, p_value