
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def task_func(data, col1, col2):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the columns exist in the DataFrame
    if col1 not in data or col2 not in data:
        raise ValueError(f"Column(s) {col1} and/or {col2} not found in the DataFrame.")
    
    # Check if the columns are categorical
    if not data[col1].dtype == "category" or not data[col2].dtype == "category":
        raise TypeError(f"One or both of the columns {col1} and/or {col2} contain non-categorical data.")
    
    # Check if the columns have multiple categories
    if len(data[col1].unique()) < 2 or len(data[col2].unique()) < 2:
        raise ValueError(f"One or both of the columns {col1} and/or {col2} do not have multiple categories.")
    
    # Check if some categories have less than 5 observations
    contingency_table = pd.crosstab(data[col1], data[col2])
    if (contingency_table.values < 5).any():
        raise ValueError("Some categories have less than 5 observations.")
    
    # Perform the chi-square test of independence
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    return p