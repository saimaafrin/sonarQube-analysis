import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def task_func(data, columns, target_column):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[columns], data[target_column], test_size=0.2, random_state=42)

    # Train logistic regression model on training data
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on testing data
    y_pred = model.predict(X_test)

    # Calculate accuracy of logistic regression model
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy
data = pd.DataFrame({'A': [0, 1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10, 11], 'C': [12, 13, 14, 15, 16, 17], 'D': [18, 19, 20, 21, 22, 23]})
columns = ['A', 'B', 'C']
target_column = 'D'