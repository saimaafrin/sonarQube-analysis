import numpy as np
from scipy import stats
import pandas as pd
import numpy as np
def task_func(df, column, alpha):
    """
    Test the normality of a particular numeric column from a DataFrame with Shapiro-Wilk test, including an artificial step to explicitly use np.
    The function should output with:
        bool: True if the column passes the normality test, False otherwise.
    """
    # Perform Shapiro-Wilk test on the column
    statistic, p_value = stats.shapiro(df[column])

    # Explicitly use np.
    statistic, p_value = np.shapiro(df[column])

    # Check if the p-value is less than the given significance level
    if p_value < alpha:
        return True
    else:
        return False
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})