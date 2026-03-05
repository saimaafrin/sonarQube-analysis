
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def task_func(data, col1, col2):
    # Check if data is empty
    if data.empty:
        raise ValueError("Data is empty")

    # Check if columns are in data
    if not (col1 in data and col2 in data):
        raise ValueError("Columns are not in data")

    # Check if columns are categorical
    if not (data[col1].dtype == "category" and data[col2].dtype == "category"):
        raise TypeError("Columns are not categorical")

    # Check if categories have enough observations
    if not (data[col1].value_counts().min() >= 5 and data[col2].value_counts().min() >= 5):
        raise ValueError("Not enough observations in categories")

    # Construct contingency table
    contingency_table = pd.crosstab(data[col1], data[col2])

    # Perform chi-square test of independence
    result = chi2_contingency(contingency_table, correction=False)

    # Return p-value
    return result.pvalue