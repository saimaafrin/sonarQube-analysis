
import pandas as pd
from statsmodels.tsa.stattools import adfuller

def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    # Filter rows where column_b is bigger than 50 and column_c is equal to 900
    filtered_df = df[(df[column_b] > 50) & (df[column_c] == 900)]

    # Check if column_a is empty after filtering or if its values are constant
    if filtered_df[column_a].empty or filtered_df[column_a].nunique() == 1:
        return True

    # Perform Augmented Dickey-Fuller test on filtered_df[column_a]
    result = adfuller(filtered_df[column_a])

    # Check if p-value is smaller than 0.05
    if result[1] < 0.05:
        return True
    else:
        return False