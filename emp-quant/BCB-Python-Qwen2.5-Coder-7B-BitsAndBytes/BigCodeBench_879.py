
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def task_func(data, col1, col2):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("The DataFrame is empty.")
    
    # Check if the specified columns exist in the DataFrame
    if col1 not in data.columns or col2 not in data.columns:
        raise ValueError(f"One or both of the columns '{col1}' and '{col2}' are not present in the DataFrame.")
    
    # Check if the columns contain categorical data
    if not data[col1].dtype == 'object' or not data[col2].dtype == 'object':
        raise TypeError(f"One or both of the columns '{col1}' and '{col2}' contain non-categorical data.")
    
    # Check if each column has multiple categories
    if len(data[col1].unique()) < 2 or len(data[col2].unique()) < 2:
        raise ValueError(f"One or both of the columns '{col1}' and '{col2}' do not have multiple categories.")
    
    # Check if any category has less than 5 observations
    contingency_table = pd.crosstab(data[col1], data[col2])
    if (contingency_table < 5).any().any():
        raise ValueError("One or more categories have less than 5 observations.")
    
    # Perform the chi-square test of independence
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    
    return p_value