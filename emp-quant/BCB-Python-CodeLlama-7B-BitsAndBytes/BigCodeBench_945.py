
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', sales_data=None):
    # Generate a time series of sales data starting from the specified date
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    sales_data = np.random.randint(100, size=periods)

    # Perform linear regression on the sales data
    X = np.arange(periods)
    y = sales_data
    lr = LinearRegression().fit(X, y)

    # Generate forecasted future sales
    forecasted_sales = lr.predict(np.arange(periods, periods + periods))

    return forecasted_sales