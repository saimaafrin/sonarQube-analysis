
import numpy as np
from scipy import stats

def task_func(df, column, alpha):
    # Perform Shapiro-Wilk test on the specified column
    statistic, p_value = stats.shapiro(df[column])

    # Check if the p-value is less than the specified significance level
    if p_value < alpha:
        return True
    else:
        return False