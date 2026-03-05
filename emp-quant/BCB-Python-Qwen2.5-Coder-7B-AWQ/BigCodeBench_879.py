import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
def task_func(data, col1, col2):
    # Check if the data is empty
    if data.empty:
        raise ValueError("The data is empty.")
    
    # Check if the columns exist in the data
    if col1 not in data.columns or col2 not in data.columns:
        raise ValueError(f"One or both of the columns ({col1}, {col2}) are not in the data.")
    
    # Check if the columns contain non-categorical data
    if not data[col1].dtype == 'object' or not data[col2].dtype == 'object':
        raise TypeError("One or both of the columns contain non-categorical data.")
    
    # Check if the columns have multiple categories
    if len(data[col1].unique()) < 2 or len(data[col2].unique()) < 2:
        raise ValueError("One or both of the columns do not have multiple categories.")
    
    # Check if some categories have less than 5 observations
    contingency_table = pd.crosstab(data[col1], data[col2])
    if (contingency_table < 5).any().any():
        raise ValueError("Some categories have less than 5 observations.")
    
    # Perform the chi-square test of independence
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)
    
    return p_value
data = pd.DataFrame({
    'a': np.random.choice(['A', 'B'], size=100),
    'b': np.random.choice(['X', 'Y'], size=100)
})