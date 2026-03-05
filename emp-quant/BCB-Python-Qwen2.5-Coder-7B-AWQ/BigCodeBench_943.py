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
    # Generate a sales time-series
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    sales = np.random.randint(100, 1000, size=periods)  # Random sales data for demonstration
    sales_series = pd.Series(sales, index=dates)

    # Decompose the time-series
    decomposition = seasonal_decompose(sales_series, model=model, period=12)  # Assuming a yearly seasonality

    # Extract the components
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Return the components as a dictionary
    return {
        'trend': trend,
        'seasonal': seasonal,
        'residual': residual
    }