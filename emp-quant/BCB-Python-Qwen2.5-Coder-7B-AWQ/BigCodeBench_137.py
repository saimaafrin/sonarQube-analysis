import pandas as pd
from scipy.stats import skew
def task_func(df):
    """
    Calculate the skewness of the last column of the dataframe.
    
    Parameters:
    df (pd.DataFrame): The input dataframe.
    
    Returns:
    float: The skewness of the last column of the dataframe.
    
    Raises:
    ValueError: If the input is not a DataFrame or has no columns.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the DataFrame has columns
    if df.empty:
        raise ValueError("DataFrame must have at least one column.")
    
    # Calculate and return the skewness of the last column
    return skew(df.iloc[:, -1])