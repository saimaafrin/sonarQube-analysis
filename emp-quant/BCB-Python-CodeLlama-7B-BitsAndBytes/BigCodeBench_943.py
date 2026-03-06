
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Generate a sales time-series
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    sales = np.random.normal(size=periods)
    sales_ts = pd.Series(sales, index=dates)

    # Decompose the time-series into trend, seasonal, and residual components
    decomposition = seasonal_decompose(sales_ts, model=model)

    # Return a dictionary containing the components
    return {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid
    }