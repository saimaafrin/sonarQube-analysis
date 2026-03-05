
import numpy as np
import pandas as pd
from scipy.stats import linregress

def task_func(df):
    """
    Perform linear regression on two variables in a DataFrame and add a 'predicted' column.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the two variables to be analyzed.
    
    Returns:
    df (pandas.DataFrame): The DataFrame with the added 'predicted' column.
    """
    # Extract the two variables from the DataFrame
    x = df['variable1']
    y = df['variable2']
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Calculate the predicted values
    df['predicted'] = slope * x + intercept
    
    return df