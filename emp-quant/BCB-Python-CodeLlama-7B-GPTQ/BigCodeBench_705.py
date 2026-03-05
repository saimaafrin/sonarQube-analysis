import numpy as np
from scipy import stats
def task_func(df, column, alpha):
    """
    Test the normality of a particular numeric column from a DataFrame with Shapiro-Wilk test.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to test.
    column : str
        The name of the column to test.
    alpha : float
        The significance level of the test.

    Returns
    -------
    bool
        True if the column passes the normality test, False otherwise.
    """
    # Perform the Shapiro-Wilk test
    statistic, p_value = stats.shapiro(df[column])

    # Check if the p-value is less than the significance level
    if p_value < alpha:
        return True
    else:
        return False
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})