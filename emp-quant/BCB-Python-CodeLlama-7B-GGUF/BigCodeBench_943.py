
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Generate a sales time-series
    sales = pd.Series(np.random.normal(100, 10, periods))

    # Decompose the time-series into trend, seasonal, and residual components
    decomposition = seasonal_decompose(sales, model=model, extrapolate_trend='freq')

    # Extract the trend, seasonal, and residual components as Pandas Series
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Return a dictionary containing the trend, seasonal, and residual components
    return {'trend': trend, 'seasonal': seasonal, 'residual': residual}