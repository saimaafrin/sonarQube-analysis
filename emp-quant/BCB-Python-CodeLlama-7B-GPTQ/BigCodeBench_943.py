import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    """
    Generate a sales time-series and decompose it into trend, seasonal, and residual components.

    Parameters
    ----------
    start_date : str, optional
        The start date of the time-series.
    periods : int, optional
        The number of periods in the time-series.
    freq : str, optional
        The frequency of the time-series.
    model : str, optional
        The type of model to use for decomposition.

    Returns
    -------
    result : dict
        A dictionary containing 'trend', 'seasonal', and 'residual' components as Pandas Series.
    """
    # Generate a random sales time-series
    np.random.seed(0)
    sales = np.random.normal(100, 10, size=periods)

    # Decompose the time-series
    decomposition = seasonal_decompose(sales, model=model, freq=freq)

    # Extract the trend, seasonal, and residual components
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Convert the components to Pandas Series
    trend = pd.Series(trend, index=pd.date_range(start_date, periods=len(trend), freq=freq))
    seasonal = pd.Series(seasonal, index=pd.date_range(start_date, periods=len(seasonal), freq=freq))
    residual = pd.Series(residual, index=pd.date_range(start_date, periods=len(residual), freq=freq))

    # Return the result as a dictionary
    return {'trend': trend, 'seasonal': seasonal, 'residual': residual}