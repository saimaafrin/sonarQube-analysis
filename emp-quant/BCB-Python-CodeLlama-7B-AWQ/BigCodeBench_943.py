import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    """
    Generate a sales time-series and decompose it into trend, seasonal, and residual components.

    Args:
        start_date (str): The start date of the time-series.
        periods (int): The number of periods in the time-series.
        freq (str): The frequency of the time-series.
        model (str): The type of model to use for decomposition.

    Returns:
        A dictionary containing 'trend', 'seasonal', and 'residual' components as Pandas Series.
    """
    # Generate a random sales time-series
    sales = pd.Series(np.random.normal(100, 10, periods))

    # Decompose the time-series
    decomposition = seasonal_decompose(sales, model=model)

    # Extract the trend, seasonal, and residual components
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Return the decomposition results as a dictionary
    return {'trend': trend, 'seasonal': seasonal, 'residual': residual}