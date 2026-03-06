
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def task_func(data, col1, col2):
    # Check if data is empty
    if data.empty:
        raise ValueError("Data is empty")

    # Check if col1 and col2 are in data
    if col1 not in data.columns or col2 not in data.columns:
        raise ValueError("One or both of the columns are not in the data")

    # Check if one or both of the columns have multiple categories
    if data[col1].nunique() <= 1 or data[col2].nunique() <= 1:
        raise ValueError("One or both of the columns do not have multiple categories")

    # Check if some categories have less than 5 observations (violating the chi-square test assumptions)
    if data[col1].value_counts().min() < 5 or data[col2].value_counts().min() < 5:
        raise ValueError("Some categories have less than 5 observations (violating the chi-square test assumptions)")

    # Check if one or both of the columns contain non-categorical data
    if not data[col1].dtype == 'category' or not data[col2].dtype == 'category':
        raise TypeError("One or both of the columns contain non-categorical data")

    # Construct contingency table
    contingency_table = pd.crosstab(data[col1], data[col2])

    # Perform chi-square test of independence
    p_value = chi2_contingency(contingency_table)[1]

    return p_value