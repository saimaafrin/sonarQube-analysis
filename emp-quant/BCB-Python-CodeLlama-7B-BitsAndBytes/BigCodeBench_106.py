
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df):
    # Check if 'df' is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' is not a valid DataFrame")

    # Check if 'date' column is in datetime format
    if 'date' not in df.columns:
        raise ValueError("'date' column is not in datetime format")

    # Convert 'date' column to ordinal
    df['date'] = pd.to_datetime(df['date']).dt.to_period('D')

    # Perform linear regression on 'value' column using 'date' column as predictor
    lr = LinearRegression()
    lr.fit(df[['date']], df['value'])

    # Make predictions on the original 'value' column
    predictions = lr.predict(df[['date']])

    # Plot the original and predicted values
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['value'], label='Original')
    ax.plot(df['date'], predictions, label='Predicted')
    ax.set_title('Value vs Date (Linear Regression Prediction)')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.legend()

    return lr, predictions, ax