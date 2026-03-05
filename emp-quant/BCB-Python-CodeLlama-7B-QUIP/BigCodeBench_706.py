
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def task_func(data, columns, target_column):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[columns], data[target_column], test_size=0.3)

    # Create a logistic regression model
    model = LogisticRegression()

    # Train the model on the training data
    model.fit(X_train, y_train)

    # Predict the target values for the testing data
    y_pred = model.predict(X_test)

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy