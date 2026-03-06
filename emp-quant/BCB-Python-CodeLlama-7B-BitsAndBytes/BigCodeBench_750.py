
import pandas as pd
import statsmodels.api as sm

def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df['Height'] > height) & (df['Weight'] < weight)]

    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None

    # Perform the OLS regression
    model = sm.OLS(filtered_df[columns[0]], filtered_df[columns[1:]])
    results = model.fit()

    # Return the results
    return results