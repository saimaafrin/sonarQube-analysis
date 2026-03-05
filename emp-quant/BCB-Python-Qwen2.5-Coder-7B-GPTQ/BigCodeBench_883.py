import pandas as pd
from statsmodels.tsa.stattools import adfuller
def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[column_b] > 50) & (df[column_c] == 900)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return True
    
    # Check if column_a is constant after filtering
    if filtered_df[column_a].nunique() == 1:
        return True
    
    # Perform the Augmented Dickey-Fuller test
    result = adfuller(filtered_df[column_a])
    
    # Check if the p-value is less than 0.05
    return result.pvalue < 0.05