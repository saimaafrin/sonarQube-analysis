
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', sales_data=None):
    # Generate time series of sales data
    if sales_data is None:
        sales_data = np.random.normal(100, 20, size=periods)
    sales_df = pd.DataFrame(sales_data, index=pd.date_range(start_date, periods=periods, freq=freq))

    # Perform linear regression on sales data
    X = sales_df.index.values.reshape(-1, 1)
    y = sales_df.values.reshape(-1, 1)
    lr = LinearRegression().fit(X, y)

    # Generate forecasted future sales
    forecasted_sales = lr.predict(X)

    return forecasted_sales