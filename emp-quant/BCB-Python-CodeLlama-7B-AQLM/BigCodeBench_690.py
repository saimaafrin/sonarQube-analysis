import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values and columns X & Y, use sklearn's linear regression to match the data to a linear model.

    Parameters:
    - df (DataFrame): The DataFrame to use.

    Returns:
    - model (LinearRegression): The fitted linear model.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.normal(size=(100, 2)), columns=['X', 'Y'])
    >>> model = task_func(df)
    >>> print(model)
    LinearRegression()
    """
    X = df['X']
    Y = df['Y']
    model = LinearRegression()
    model.fit(X, Y)
    return model