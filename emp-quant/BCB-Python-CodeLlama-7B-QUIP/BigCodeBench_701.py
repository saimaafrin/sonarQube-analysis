
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target):
    # Perform linear regression analysis on the given DataFrame
    model = LinearRegression().fit(df, target)
    # Return the R-squared score of the model
    return model.score()