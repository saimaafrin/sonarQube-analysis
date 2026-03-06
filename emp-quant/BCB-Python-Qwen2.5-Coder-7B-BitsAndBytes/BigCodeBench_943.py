
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Create a date range
    dates = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate a random sales data series
    np.random.seed(0)  # For reproducibility
    sales_data = np.cumsum(np.random.randn(periods)) * 100
    
    # Decompose the sales data
    decomposition = seasonal_decompose(sales_data, model=model, period=freq_to_period(freq))
    
    # Extract the trend, seasonal, and residual components
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    
    # Return the results as a dictionary of Pandas Series
    return {
        'trend': pd.Series(trend, index=dates),
        'seasonal': pd.Series(seasonal, index=dates),
        'residual': pd.Series(residual, index=dates)
    }

# Helper function to convert frequency string to period
def freq_to_period(freq):
    if freq == 'D':
        return 7
    elif freq == 'W':
        return 52
    elif freq == 'M':
        return 12
    else:
        raise ValueError("Unsupported frequency")