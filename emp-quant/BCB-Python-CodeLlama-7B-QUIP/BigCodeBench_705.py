
import numpy as np
from scipy import stats

def task_func(df, column, alpha):
    # Perform Shapiro-Wilk test on the given column
    shapiro_result = stats.shapiro(df[column])
    # Calculate the p-value
    p_value = shapiro_result[1]
    # Check if the p-value is greater than the given alpha value
    if p_value > alpha:
        return False
    else:
        return True