import pandas as pd
import seaborn as sns
from scipy import stats
def task_func(data):
    """
    Processes a given dataset to compute the average of each row, plots the distribution of these averages,
    and evaluates their normality. The function returns these averages as an additional column in a DataFrame,
    the plot of the distribution, and the p-value from the normality test if applicable.
    
    Parameters:
    data (pd.DataFrame): Input DataFrame with exactly eight columns.
    
    Returns:
    tuple: Contains three elements:
        - DataFrame: A pandas DataFrame with the original data and an added 'Average' column.
        - Axes object: The Axes object from the seaborn distribution plot of the averages.
        - float or None: The p-value from the normality test on the averages, or None if the test could not be conducted.
    """
    # Check if the input data has exactly eight columns
    if data.shape[1] != 8:
        raise ValueError("Input data must have exactly eight columns.")
    
    # Compute the average of each row
    data['Average'] = data.mean(axis=1)
    
    # Plot the distribution of the averages
    plot = sns.distplot(data['Average'])
    
    # Evaluate normality if there are at least 20 data points
    if len(data['Average']) >= 20:
        _, p_value = stats.normaltest(data['Average'])
    else:
        p_value = None
    
    return data, plot, p_value