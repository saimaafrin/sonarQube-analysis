
import numpy as np
from scipy import stats

def task_func(df, column, alpha):
    """
    Test the normality of a particular numeric column from a DataFrame using the Shapiro-Wilk test.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.
    column (str): The name of the column to test for normality.
    alpha (float): The significance level for the test.

    Returns:
    bool: True if the column passes the normality test at the given alpha level, False otherwise.
    """
    # Extract the column data
    data = df[column]
    
    # Perform the Shapiro-Wilk test
    stat, p_value = stats.shapiro(data)
    
    # Determine if the column passes the normality test
    result = p_value > alpha
    
    return result