import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df, target):
    """
    Perform a linear regression analysis on a given DataFrame.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing the features and target.
    target (str): The name of the target column.
    
    Returns:
    float: The R-squared score of the model.
    """
    # Separate features and target
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Initialize and fit the Linear Regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Calculate the R-squared score
    score = model.score(X, y)
    
    return score