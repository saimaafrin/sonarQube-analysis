
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target):
    # Splitting the DataFrame into features and target variable
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Creating a linear regression model
    model = LinearRegression()
    
    # Fitting the model to the data
    model.fit(X, y)
    
    # Calculating the R-squared score of the model
    score = model.score(X, y)
    
    return score