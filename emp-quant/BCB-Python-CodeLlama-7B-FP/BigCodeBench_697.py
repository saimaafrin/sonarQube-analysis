import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import pytest
def task_func(df):
    X = df['feature']
    y = df['value']
    model = LinearRegression()
    model.fit(X, y)
    result = {'coefficients': model.coef_, 'intercept': model.intercept_}
    return result