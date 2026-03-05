import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def task_func(df):
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Check if 'date' and 'value' columns exist
    required_columns = ['date', 'value']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("DataFrame must contain 'date' and 'value' columns")
    
    # Check if 'date' column is in datetime format
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("'date' column must be in datetime format")
    
    # Convert 'date' to ordinal
    df['date'] = df['date'].map(pd.Timestamp.toordinal)
    
    # Prepare data for linear regression
    X = df[['date']]
    y = df['value']
    
    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions
    predictions = model.predict(X)
    
    # Plotting
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['value'], label='Original Data')
    ax.plot(df['date'], predictions, label='Predicted Data', linestyle='--')
    ax.set_title('Value vs Date (Linear Regression Prediction)')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')
    ax.legend()
    
    return model, predictions, ax