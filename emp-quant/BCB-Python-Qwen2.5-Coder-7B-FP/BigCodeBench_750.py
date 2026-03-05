import pandas as pd
import statsmodels.api as sm
def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    """
    Performs an OLS linear regression on a subset of the provided DataFrame.
    
    Parameters:
    - df: pandas DataFrame containing the data.
    - height: int, the threshold for the 'Height' column.
    - weight: int, the threshold for the 'Weight' column.
    - columns: list, the column names to be used in the regression.
    
    Returns:
    - sm.regression.linear_model.RegressionResultsWrapper: The result of the OLS regression, or None if no rows meet the criteria or DataFrame is empty.
    """
    if df.empty:
        return None
    
    # Filter rows based on the conditions
    filtered_df = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]
    
    if filtered_df.empty:
        return None
    
    # Prepare the dependent variable and independent variables
    y = filtered_df[columns[0]]
    X = filtered_df[columns[1:]]
    X = sm.add_constant(X)  # Adding a constant for the intercept
    
    # Perform OLS regression
    model = sm.OLS(y, X).fit()
    
    return model
df = pd.DataFrame(np.random.randint(10,98,size=(100, 3)), columns=['Age', 'Height', 'Weight'])