
import pandas as pd
import statsmodels.api as sm

def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    # Filter rows where the value in the second column is greater than 'height' and the value in the third column is less than 'weight'
    filtered_df = df[df[columns[1]] > height]
    filtered_df = filtered_df[filtered_df[columns[2]] < weight]

    # If the filtered DataFrame is empty, return None
    if filtered_df.empty:
        return None

    # Perform OLS linear regression on the filtered DataFrame
    model = sm.OLS(filtered_df[columns[0]], filtered_df[columns[1:]])
    results = model.fit()

    return results