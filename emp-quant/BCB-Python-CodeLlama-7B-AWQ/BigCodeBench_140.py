import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest
def task_func(df, cols):
    """
    Standardize specified numeric columns in a dataframe.

    Args:
        df (pd.DataFrame): The dataframe to be standardized.
        cols (list): The list of columns to be standardized.

    Returns:
        pd.DataFrame: The dataframe with standardized columns.

    Raises:
        ValueError: If 'df' is not a DataFrame, 'cols' is not a list, or columns in 'cols' don't exist in 'df'.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas DataFrame")
    if not isinstance(cols, list):
        raise ValueError("'cols' must be a list")
    if not all(col in df.columns for col in cols):
        raise ValueError("columns in 'cols' don't exist in 'df'")

    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df[cols])
    scaled_df = pd.DataFrame(scaled_df, columns=cols)
    return scaled_df