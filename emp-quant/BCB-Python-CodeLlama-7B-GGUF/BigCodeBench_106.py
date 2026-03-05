
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df):
    # Check if 'df' is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a valid DataFrame")

    # Check if 'df' has the required columns
    required_columns = ['date', 'value']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("'df' must have columns 'date' and 'value'")

    # Check if 'date' column is in datetime format
    if not pd.to_datetime(df['date']).equals(df['date']):
        raise ValueError("'date' column must be in datetime format")

    # Convert 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).dt.to_period('D')

    # Perform linear regression
    X = df['date']
    y = df['value']
    model = LinearRegression().fit(X, y)

    # Make predictions
    X_pred = pd.date_range(start=X.min(), end=X.max(), freq='D')
    y_pred = model.predict(X_pred)

    # Plot original and predicted values
    fig, ax = plt.subplots()
    ax.plot(X, y, label='Original')
    ax.plot(X_pred, y_pred, label='Predicted')
    ax.set_title('Value vs Date (Linear Regression Prediction)')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.legend()

    return model, y_pred, ax