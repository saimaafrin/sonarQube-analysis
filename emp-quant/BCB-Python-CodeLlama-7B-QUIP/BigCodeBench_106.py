
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df):
    # Check if df is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a valid DataFrame")

    # Check if df has the required columns
    if not set(['date', 'value']).issubset(set(df.columns)):
        raise ValueError("df must have columns 'date' and 'value'")

    # Check if 'date' column is in datetime format
    if not df['date'].dtype == 'datetime64[ns]':
        raise ValueError("'date' column must be in datetime format")

    # Perform linear regression
    model = LinearRegression().fit(df[['date', 'value']], df['value'])

    # Get predictions for the entire dataset
    predictions = model.predict(df[['date', 'value']])

    # Plot the original and predicted values
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['value'], 'bo-', label='Original')
    ax.plot(df['date'], predictions, 'ro-', label='Predicted')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.set_title('Value vs Date (Linear Regression Prediction)')
    ax.legend()
    return (model, predictions, ax)