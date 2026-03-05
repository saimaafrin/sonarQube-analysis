import pandas as pd
from statsmodels.tsa.stattools import adfuller
def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    """
    Determines if a specific subset of data is stationary by filtering rows where column_b bigger than 50 and column_c equal to 900. Data is considered to be stationary if the p_value returned by the Augmented Dickey-Fuller test is smaller than 0.05. If column_a is empty after filtering or if its values are constant, True is returned.
    """
    # Filter rows where column_b bigger than 50 and column_c equal to 900
    df_filtered = df[(df[column_b] > 50) & (df[column_c] == 900)]

    # Check if column_a is empty after filtering
    if df_filtered[column_a].empty:
        return True

    # Check if column_a values are constant
    if df_filtered[column_a].nunique() == 1:
        return True

    # Perform Augmented Dickey-Fuller test
    result = adfuller(df_filtered[column_a])

    # Check p-value
    if result[1] < 0.05:
        return True
    else:
        return False
df = pd.DataFrame({
    "column_a": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "column_b": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    "column_c": [900, 900, 900, 900, 900, 900, 900, 900, 900, 900]
})