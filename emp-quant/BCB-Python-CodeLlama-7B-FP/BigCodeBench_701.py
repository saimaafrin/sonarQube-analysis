import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df, target):
    """
    Perform a linear regression analysis on a given DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to perform the regression on.
        target (str): The name of the target variable.

    Returns:
        score (float): The R-squared score of the model.
    """
    X = df.drop(columns=target)
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    score = model.score(X, y)
    return score
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'C': [3, 6, 9, 12, 15],
    'target': [4, 8, 12, 16, 20]
})