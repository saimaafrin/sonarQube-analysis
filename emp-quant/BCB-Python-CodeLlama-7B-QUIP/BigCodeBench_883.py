
import pandas as pd
from statsmodels.tsa.stattools import adfuller

def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    # Filter the data based on column_b and column_c
    filtered_data = df.loc[df[column_b] > 50 & df[column_c] == 900]

    # Check if column_a is empty or constant
    if filtered_data[column_a].empty or filtered_data[column_a].nunique == 1:
        return True

    # Perform the Augmented Dickey-Fuller test
    result = adfuller(filtered_data[column_a])

    # Check the p-value
    if result[1] < 0.05:
        return True
    else:
        return False