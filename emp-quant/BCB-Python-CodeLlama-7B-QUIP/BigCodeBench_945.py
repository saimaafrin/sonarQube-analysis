
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def task_func(start_date='2016-01-01', periods=13, freq='WOM-2FRI', sales_data=None):
    # Load the sales data
    if sales_data is None:
        sales_data = pd.DataFrame({
            'date': ['2016-01-01', '2016-01-08', '2016-01-15', '2016-01-22', '2016-01-29', '2016-02-05', '2016-02-12', '2016-02-19', '2016-02-26', '2016-03-05', '2016-03-12', '2016-03-19', '2016-03-26'],
            'sales': [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]
        })

    # Create a time series of dates
    dates = pd.date_range(start_date, periods=periods, freq=freq)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(sales_data['date'], sales_data['sales'])

    # Make predictions for the future dates
    predictions = model.predict(dates)

    # Return the predictions
    return predictions