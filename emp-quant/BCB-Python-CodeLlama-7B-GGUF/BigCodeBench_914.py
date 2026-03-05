
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def task_func(df):
    # Split the data into training and testing sets
    X = df.drop(columns=['Close'])
    y = df['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a LinearRegression model and fit the data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Create a new dataframe with the predicted prices
    df_pred = pd.DataFrame({'Close': y_pred})

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Close'], label='Actual')
    ax.plot(df_pred['Date'], df_pred['Close'], label='Predicted')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close')
    ax.legend()
    plt.show()

    # Return the predicted prices and the matplotlib Axes object
    return y_pred, ax

# Load the stock data
df = pd.read_csv('stock_data.csv')

# Call the task function and get the predicted prices and the matplotlib Axes object
y_pred, ax = task_func(df)

# Print the predicted prices
print(y_pred)