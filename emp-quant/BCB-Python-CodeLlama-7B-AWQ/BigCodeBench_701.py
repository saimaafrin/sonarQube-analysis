import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def task_func(df, target):
    """
    Perform a linear regression analysis on a given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to perform the regression on.
        target (str): The name of the target column.

    Returns:
        score (float): The R-squared score of the model.
    """
    X = df.drop(columns=target)
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    score = r2_score(y, y_pred)
    return score
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'target': [10, 20, 30, 40, 50]
})