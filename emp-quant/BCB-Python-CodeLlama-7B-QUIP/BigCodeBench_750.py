
import pandas as pd
import statsmodels.api as sm

def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    # Check if DataFrame is empty
    if df.empty:
        return None

    # Filter rows where the value in the second column of 'columns' is greater than 'height' and the value in the third column is less than 'weight'
    df_subset = df[df[columns[1]] > height]
    df_subset = df_subset[df_subset[columns[2]] < weight]

    # Perform OLS linear regression on the subset
    model = sm.OLS(df_subset[columns[0]], df_subset[columns[1:]])
    results = model.fit()

    # Return the results of the OLS regression
    return results