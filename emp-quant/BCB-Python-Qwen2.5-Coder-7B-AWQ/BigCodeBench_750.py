import pandas as pd
import statsmodels.api as sm
def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    # Check if the DataFrame is empty
    if df.empty:
        return None
    
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]
    
    # Check if there are any rows that meet the conditions
    if filtered_df.empty:
        return None
    
    # Prepare the dependent variable (y) and independent variables (X)
    y = filtered_df[columns[0]]
    X = filtered_df[columns[1:]]
    
    # Add a constant to the independent variables for the intercept
    X = sm.add_constant(X)
    
    # Perform the OLS regression
    model = sm.OLS(y, X).fit()
    
    return model