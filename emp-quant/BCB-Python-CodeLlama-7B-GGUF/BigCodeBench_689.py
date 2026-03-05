
import numpy as np
from scipy import stats

def task_func(df):
    # Perform Shapiro-Wilk test on each column of the DataFrame
    p_values = {}
    for col in df.columns:
        stat, p = stats.shapiro(df[col])
        p_values[col] = p

    # Return a dictionary with p-values from the Shapiro-Wilk test for each column
    return p_values