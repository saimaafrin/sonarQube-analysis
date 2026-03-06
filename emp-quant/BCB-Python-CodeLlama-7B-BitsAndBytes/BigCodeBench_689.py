
import numpy as np
from scipy import stats

def task_func(df):
    # Initialize an empty dictionary to store the p-values
    p_values = {}

    # Loop through each column of the DataFrame
    for col in df.columns:
        # Perform the Shapiro-Wilk test on the column
        result = stats.shapiro(df[col])

        # Extract the p-value from the result
        p_value = result[1]

        # Add the p-value to the dictionary
        p_values[col] = p_value

    # Return the dictionary of p-values
    return p_values