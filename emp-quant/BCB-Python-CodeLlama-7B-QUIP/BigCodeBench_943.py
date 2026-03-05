
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(start_date='2016-01-01', periods=24, freq='M', model='additive'):
    # Generate a random time-series
    np.random.seed(0)
    data = pd.Series(np.random.normal(size=24))

    # Decompose the time-series into trend, seasonal, and residual components
    decomposition = seasonal_decompose(data, model=model, freq=freq, periods=periods)

    # Return a dictionary containing the trend, seasonal, and residual components
    return {
        'trend': decomposition.trend,
        'seasonal': decomposition.seasonal,
        'residual': decomposition.residual
    }

# Print the length of the seasonal component
print(len(result['seasonal']))