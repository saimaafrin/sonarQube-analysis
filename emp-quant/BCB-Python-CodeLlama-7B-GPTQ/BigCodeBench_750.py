import pandas as pd
import statsmodels.api as sm
def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    """
    Performs an OLS linear regression on a subset of the provided DataFrame.
    The subset is created by filtering rows where the value in the second column of 'columns' is greater than 'height' and the value in the third column is less than 'weight'.
    The first column in 'columns' is used as the dependent variable / target (y), and the rest as independent variables (X) in the regression.
    If df is empty, or if no rows match the conditions None is returned.
    """
    # Check if the DataFrame is empty
    if df.empty:
        return None

    # Filter the rows based on the conditions
    filtered_df = df[df[columns[1]] > height]
    filtered_df = filtered_df[filtered_df[columns[2]] < weight]

    # Perform the OLS regression
    model = sm.OLS(filtered_df[columns[0]], filtered_df[columns[1:]])
    results = model.fit()

    # Return the results
    return results
df = pd.DataFrame(np.random.randint(10, 98, size=(100, 3)), columns=['Age', 'Height', 'Weight'])