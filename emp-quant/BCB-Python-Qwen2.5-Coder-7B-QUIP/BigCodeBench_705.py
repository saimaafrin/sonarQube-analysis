
import numpy as np
from scipy import stats

def task_func(df, column, alpha):
    # Extract the column data as a numpy array
    data = df[column].dropna().values
    
    # Perform the Shapiro-Wilk test
    _, p_value = stats.shapiro(data)
    
    # Determine if the column passes the normality test
    result = p_value >= alpha
    
    return result