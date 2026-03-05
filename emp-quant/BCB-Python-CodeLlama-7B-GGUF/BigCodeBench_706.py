
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def task_func(data, columns, target_column):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[columns], data[target_column], test_size=0.2, random_state=42)
    
    # Train a logistic regression model on the training data
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the testing data
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy