
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target):
    # Perform linear regression on the given DataFrame
    X = df.drop(target, axis=1)
    y = df[target]
    model = LinearRegression().fit(X, y)

    # Calculate the R-squared score of the model
    score = model.score(X, y)

    return score