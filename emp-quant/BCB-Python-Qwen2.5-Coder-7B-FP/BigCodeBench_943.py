import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    """
    Generate a sales time-series and decompose it into trend, seasonal, and residual components.

    Parameters:
    - start_date (str): The start date of the time-series.
    - periods (int): The number of periods in the time-series.
    - freq (str): The frequency of the time-series (e.g., 'M' for monthly).
    - model (str): The decomposition model ('additive' or 'multiplicative').

    Returns:
    - dict: A dictionary containing 'trend', 'seasonal', and 'residual' components as Pandas Series.
    """
    # Generate a time-series with a multiplicative seasonal pattern
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    sales = np.random.rand(periods) * 100  # Random sales data
    seasonal = np.sin(np.linspace(0, 2 * np.pi, periods)) * 50  # Sinusoidal seasonal pattern
    trend = np.linspace(0, 10, periods)  # Linear trend
    noise = np.random.normal(0, 10, periods)  # Gaussian noise
    if model == 'multiplicative':
        sales = sales * seasonal * trend * noise
    else:
        sales = sales + seasonal + trend + noise
    
    # Decompose the time-series
    decomposition = seasonal_decompose(sales, model=model, period=freq)
    
    # Return the decomposition components as a dictionary
    return {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.resid
    }