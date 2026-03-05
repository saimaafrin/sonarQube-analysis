import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df, target):
    """
    Perform a linear regression analysis on a given DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame containing the features and target variable.
    - target (str): The name of the target variable column in the DataFrame.
    
    Returns:
    - score (float): The R-squared score of the model.
    """
    # Separate the features and target variable
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Initialize the Linear Regression model
    model = LinearRegression()
    
    # Fit the model
    model.fit(X, y)
    
    # Calculate the R-squared score
    score = model.score(X, y)
    
    return score