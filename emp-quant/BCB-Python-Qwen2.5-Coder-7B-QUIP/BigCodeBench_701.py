
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def task_func(df, target):
    # Ensure the target column is in the DataFrame
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in the DataFrame.")
    
    # Split the DataFrame into features and target
    X = df.drop(target, axis=1)
    y = df[target]
    
    # Initialize the LinearRegression model
    model = LinearRegression()
    
    # Fit the model
    model.fit(X, y)
    
    # Predict using the model
    predictions = model.predict(X)
    
    # Calculate the R-squared score
    score = r2_score(y, predictions)
    
    return score