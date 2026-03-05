
import numpy as np
from scipy import stats

def task_func(df):
    # Initialize the dictionary to store the p-values
    p_values = {}

    # Loop through each column of the DataFrame
    for column in df:
        # Perform the Shapiro-Wilk test on the column
        shapiro_result = stats.shapiro(df[column])
        # Add the p-value to the dictionary
        p_values[column] = shapiro_result.pvalue

    # Return the dictionary of p-values
    return p_values