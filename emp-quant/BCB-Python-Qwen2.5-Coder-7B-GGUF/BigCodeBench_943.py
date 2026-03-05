
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate a sales time-series with a trend and seasonal component
    trend = np.linspace(0, 1, periods)
    seasonal = np.sin(np.linspace(0, 2 * np.pi, periods))
    sales = trend + seasonal
    
    # Add noise to the sales data
    noise = np.random.normal(0, 0.1, periods)
    sales += noise
    
    # Decompose the sales time-series
    decomposition = seasonal_decompose(sales, model=model, period=freq)
    
    # Return the trend, seasonal, and residual components as Pandas Series
    result = {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid
    }
    
    return result