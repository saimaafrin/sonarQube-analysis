
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Generate a sales time-series
    np.random.seed(42)  # For reproducibility
    time_index = pd.date_range(start_date, periods=periods, freq=freq)
    sales_data = np.random.exponential(scale=10, size=periods) + np.sin(np.arange(periods) * 2 * np.pi / 24) * 50
    sales_series = pd.Series(sales_data, index=time_index)

    # Decompose the time-series
    decomposition = seasonal_decompose(sales_series, model=model, periods=periods)

    # Extract the trend, seasonal, and residual components
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Return the components as a dictionary
    return {'trend': trend, 'seasonal': seasonal, 'residual': residual}