import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', sales_data=None):
    """
    Generates a time series of sales data starting from a specified date, then uses linear regression to forecast future sales based on the provided or generated sales data.

    Args:
        start_date (str): The starting date of the time series.
        periods (int): The number of periods to generate.
        freq (str): The frequency of the time series.
        sales_data (pd.Series): The sales data to use for forecasting.

    Returns:
        A numpy array containing the forecasted future sales for the same number of periods as the input data.
    """
    # Generate a time series of sales data
    if sales_data is None:
        sales_data = pd.Series(np.random.normal(100, 10, periods))
    else:
        sales_data = pd.Series(sales_data)

    # Create a pandas DataFrame with the time series data
    df = pd.DataFrame({'date': pd.date_range(start_date, periods=periods, freq=freq),
                       'sales': sales_data})

    # Fit a linear regression model to the data
    model = LinearRegression()
    model.fit(df['date'], df['sales'])

    # Make predictions for the future periods
    future_dates = pd.date_range(df['date'].iloc[-1], periods=periods, freq=freq)
    forecast = model.predict(future_dates)

    return forecast
start_date = '2016-01-01'
periods = 13
freq = 'WOM-2FRI'
sales_data = None