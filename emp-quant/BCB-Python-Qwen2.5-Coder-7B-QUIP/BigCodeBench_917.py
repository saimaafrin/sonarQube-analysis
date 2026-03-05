
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Ensure the DataFrame has a datetime index
    df.set_index('date', inplace=True)
    
    # Fit the ARIMA model
    model = ARIMA(df['close'], order=(5, 1, 0))
    model_fit = model.fit()
    
    # Forecast the next 7 days
    forecast, _ = model_fit.forecast(7)
    
    # Plot the forecast
    fig, ax = plt.subplots()
    ax.plot(df['close'], label='Actual')
    ax.plot(pd.date_range(start=df.index[-1], periods=8, closed='right'), pd.Series(forecast, name='Forecast'), label='Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    ax.legend()
    
    return forecast, ax