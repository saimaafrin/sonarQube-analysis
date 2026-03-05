
import pandas as pd
import statsmodels.api as sm

def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    if df.empty:
        return None

    subset = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]

    if subset.empty:
        return None

    y = subset[columns[0]]
    X = subset[columns[1]:].values

    # Adding a constant to the model
    X = sm.add_constant(X)

    results = sm.OLS(y, X).fit()

    return results