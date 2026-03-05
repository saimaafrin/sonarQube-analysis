import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
def task_func(data):
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(data['Hours'], data['Scores'], test_size=0.2, random_state=42)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate mean squared error
    mse = np.mean((y_test - y_pred) ** 2)

    return mse
data = pd.DataFrame({'Hours': [1, 2, 3, 4, 5], 'Scores': [10, 20, 30, 40, 50]})