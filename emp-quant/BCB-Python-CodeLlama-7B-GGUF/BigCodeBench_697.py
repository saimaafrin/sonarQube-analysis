
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(df):
    X = df['feature']
    y = df['value']
    model = LinearRegression()
    model.fit(X, y)
    result = {'coefficients': model.coef_, 'intercept': model.intercept_}
    return result