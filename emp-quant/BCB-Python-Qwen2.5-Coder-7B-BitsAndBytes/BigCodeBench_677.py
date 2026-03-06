
import numpy as np
import pandas as pd
from scipy.stats import linregress

def task_func(df, x_col, y_col):
    """
    Perform linear regression on two columns of a DataFrame and add a 'predicted' column.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    x_col (str): The name of the column to use as the independent variable.
    y_col (str): The name of the column to use as the dependent variable.

    Returns:
    df (pandas.DataFrame): The DataFrame with an additional 'predicted' column containing the predicted values.
    """
    # Extract the data for the specified columns
    x = df[x_col].values
    y = df[y_col].values
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Create a new column with the predicted values
    df['predicted'] = slope * x + intercept
    
    return df

    # Call the function
    result_df = task_func(df, 'x', 'y')
    
    print(result_df)