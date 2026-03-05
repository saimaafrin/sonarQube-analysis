
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def task_func(data):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(data['Hours'], data['Scores'], test_size=0.2, random_state=42)

    # Train a simple linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate the mean squared error
    mse = np.mean((y_test - y_pred) ** 2)

    return mse

# Load the data
data = pd.read_csv('data.csv')

# Call the task function
mse = task_func(data)

# Print the mean squared error
print(mse)