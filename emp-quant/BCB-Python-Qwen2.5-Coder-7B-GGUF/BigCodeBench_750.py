
import pandas as pd
import statsmodels.api as sm

def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    if df.empty:
        return None
    
    # Filter rows based on the conditions
    subset_df = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]
    
    if subset_df.empty:
        return None
    
    # Prepare the dependent variable (y) and independent variables (X)
    y = subset_df[columns[0]]
    X = subset_df[columns[1:]]
    
    # Add a constant to the independent variables
    X = sm.add_constant(X)
    
    # Perform OLS regression
    model = sm.OLS(y, X).fit()
    
    return model