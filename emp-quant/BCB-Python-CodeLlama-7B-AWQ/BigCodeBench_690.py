import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import pytest
COLUMNS = ['X', 'Y']
def task_func(df):
    X = df[COLUMNS[0]]
    y = df[COLUMNS[1]]
    model = LinearRegression()
    model.fit(X, y)
    return model