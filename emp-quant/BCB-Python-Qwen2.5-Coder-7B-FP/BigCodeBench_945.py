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
    - sales_data (np.array): Optional numpy array of sales data to use for forecasting.
    
    Returns:
    - np.array: A numpy array containing the forecasted future sales for the same number of periods as the input data.
    """
    # Generate time series if no sales data is provided
    if sales_data is None:
        date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
        sales_data = np.random.randint(100, 500, size=periods)
    
    # Create a DataFrame for the time series
    df = pd.DataFrame(sales_data, index=date_range, columns=['Sales'])
    
    # Fit a linear regression model
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['Sales']
    model = LinearRegression().fit(X, y)
    
    # Forecast future sales
    future_X = np.arange(len(df), len(df) + periods).reshape(-1, 1)
    future_sales = model.predict(future_X)
    
    return future_sales
start_date = '2016-01-01'
periods = 13
freq = 'WOM-2FRI'
sales_data = None