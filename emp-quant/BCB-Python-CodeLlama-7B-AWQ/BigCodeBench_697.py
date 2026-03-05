import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import pytest
def task_func(df):
    """
    Use a linear regression model to predict the "value" of "feature" in the given dataframe and return the coefficients and intercept.
    """
    X = df['feature']
    y = df['value']
    model = LinearRegression()
    model.fit(X, y)
    result = {
        'coefficients': model.coef_,
        'intercept': model.intercept_
    }
    return result