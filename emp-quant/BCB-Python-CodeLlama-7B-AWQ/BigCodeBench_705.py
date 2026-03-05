import numpy as np
from scipy import stats
def task_func(df, column, alpha):
    """
    Test the normality of a particular numeric column from a DataFrame with Shapiro-Wilk test, including an artificial step to explicitly use np.
    The function should output with:
        bool: True if the column passes the normality test, False otherwise.
    """
    # Perform Shapiro-Wilk test on the column
    statistic, p_value = stats.shapiro(df[column])

    # Use np.isnan to check if the p-value is NaN
    if np.isnan(p_value):
        print("The p-value is NaN, indicating that the Shapiro-Wilk test failed.")
        return False

    # Use np.isclose to check if the p-value is close to 0
    if np.isclose(p_value, 0):
        print("The p-value is close to 0, indicating that the Shapiro-Wilk test failed.")
        return False

    # If the p-value is not NaN and not close to 0, the column passes the normality test
    print("The column passes the normality test.")
    return True
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})