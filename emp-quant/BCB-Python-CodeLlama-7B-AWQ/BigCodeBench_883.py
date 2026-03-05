import pandas as pd
from statsmodels.tsa.stattools import adfuller
import pytest
def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    """
    Determines if a specific subset of data is stationary by filtering rows where column_b bigger than 50 and column_c equal to 900. Data is considered to be stationary if the p_value returned by the Augmented Dickey-Fuller test is smaller than 0.05. If column_a is empty after filtering or if its values are constant, True is returned.
    """
    # Filter rows where column_b bigger than 50 and column_c equal to 900
    filtered_df = df.loc[(df[column_b] > 50) & (df[column_c] == 900)]

    # Check if column_a is empty after filtering or if its values are constant
    if filtered_df[column_a].empty or filtered_df[column_a].is_unique:
        return True

    # Perform Augmented Dickey-Fuller test on filtered data
    result = adfuller(filtered_df[column_a])

    # Check if p_value is smaller than 0.05
    if result[1] < 0.05:
        return True
    else:
        return False