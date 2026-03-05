import numpy as np
import pandas as pd
from scipy.stats import linregress
def task_func(df):
    """
    Perform linear regression on two variables in a DataFrame and add a 'predicted' column.
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing at least two numeric columns.
    
    Returns:
    df (pandas.DataFrame): DataFrame with an additional 'predicted' column containing the regression predictions.
    """
    # Extract the two variables for regression
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Create a new column 'predicted' with the regression predictions
    df['predicted'] = slope * x + intercept
    
    return df