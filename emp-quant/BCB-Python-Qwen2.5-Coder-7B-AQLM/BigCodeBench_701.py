
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(df, target):
    # Split the DataFrame into features and target variable
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Initialize the LinearRegression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    # Calculate the R-squared score of the model
    score = model.score(X, y)
    
    return score