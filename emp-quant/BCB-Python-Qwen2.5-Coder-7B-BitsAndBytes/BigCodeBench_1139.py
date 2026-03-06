
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def task_func(data):
    # Splitting the data into features (X) and target (y)
    X = data[['Hours']]
    y = data['Scores']
    
    # Splitting the dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Creating a linear regression model
    model = LinearRegression()
    
    # Training the model
    model.fit(X_train, y_train)
    
    # Predicting the test set results
    y_pred = model.predict(X_test)
    
    # Calculating the Mean Squared Error
    mse = np.mean((y_test - y_pred) ** 2)
    
    return mse