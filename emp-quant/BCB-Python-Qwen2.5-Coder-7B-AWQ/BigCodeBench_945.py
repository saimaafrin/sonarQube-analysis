import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', sales_data=None):
    """
    Generates a time series of sales data starting from a specified date, then uses linear regression to forecast future sales.
    
    Parameters:
    - start_date (str): The starting date of the time series in 'YYYY-MM-DD' format.
    - periods (int): The number of periods to generate or forecast.
    - freq (str): The frequency of the time series, e.g., 'WOM-2FRI' for the second Friday of each month.
    - sales_data (np.array): An array of sales data to use for forecasting. If None, generates synthetic data.
    
    Returns:
    - np.array: An array containing the forecasted future sales for the same number of periods as the input data.
    """
    # Generate synthetic sales data if none is provided
    if sales_data is None:
        dates = pd.date_range(start=start_date, periods=periods, freq=freq)
        sales_data = np.random.randint(100, 500, size=periods)
    
    # Create a DataFrame with dates and sales data
    df = pd.DataFrame({'date': dates, 'sales': sales_data})
    
    # Convert the date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Set the date column as the index
    df.set_index('date', inplace=True)
    
    # Fit a linear regression model
    X = df.index.values.reshape(-1, 1)
    y = df['sales'].values
    model = LinearRegression().fit(X, y)
    
    # Forecast future sales
    future_dates = pd.date_range(start=dates[-1], periods=periods, freq=freq)
    future_X = future_dates.values.reshape(-1, 1)
    future_sales = model.predict(future_X)
    
    return future_sales
start_date = '2016-01-01'
periods = 13
freq = 'WOM-2FRI'
sales_data = None