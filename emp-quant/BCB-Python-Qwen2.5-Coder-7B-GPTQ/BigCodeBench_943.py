import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Create a date range
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Generate a sales time-series with a multiplicative model
    np.random.seed(0)  # For reproducibility
    trend = np.linspace(1, 10, periods)
    seasonal = np.sin(np.linspace(0, 2 * np.pi, periods))
    noise = np.random.normal(0, 0.1, periods)
    sales = trend * seasonal * (1 + noise)
    
    # Create a DataFrame
    df = pd.DataFrame(sales, index=date_range, columns=['sales'])
    
    # Decompose the time-series
    decomposition = seasonal_decompose(df['sales'], model=model, period=freq)
    
    # Extract the components
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    
    # Return the result as a dictionary
    result = {
        'trend': trend,
        'seasonal': seasonal,
        'residual': residual
    }
    
    return result