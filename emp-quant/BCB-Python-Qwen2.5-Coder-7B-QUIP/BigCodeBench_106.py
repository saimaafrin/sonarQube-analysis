
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df):
    # Check if df is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame")
    
    # Check if required columns exist
    if 'date' not in df or 'value' not in df:
        raise ValueError("DataFrame must contain 'date' and 'value' columns")
    
    # Convert 'date' to ordinal
    df['date_ordinal'] = pd.to_datetime(df['date']).astype(int)
    
    # Initialize the LinearRegression model
    model = LinearRegression()
    
    # Fit the model
    model.fit(df[['date_ordinal']], df['value'])
    
    # Predict values
    predictions = model.predict(df[['date_ordinal']])
    
    # Plot the original and predicted values
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['value'], 'o', label='Original')
    ax.plot(df['date'], predictions, 'r-', label='Predicted')
    ax.set_title('Value vs Date (Linear Regression Prediction)')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.legend()
    
    # Return the model, predictions, and axes object
    return model, predictions, ax