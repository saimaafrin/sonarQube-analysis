import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple
def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    """
    Forecast the share closing prices for the next 7 days using the ARIMA model and plot the forecast.

    Parameters:
    df (pd.DataFrame): DataFrame containing the historical share closing prices.

    Returns:
    Tuple[List[float], Axes]: A tuple containing:
        A list with forecasted prices for the next 7 days.
        A matplotlib Axes object containing the subplot.
    """
    # Ensure the DataFrame has a datetime index
    df.set_index('date', inplace=True)
    
    # Fit the ARIMA model
    model = ARIMA(df['close'], order=(5,1,0))
    model_fit = model.fit()
    
    # Forecast the next 7 days
    forecast = model_fit.forecast(steps=7)
    forecast_list = forecast.tolist()
    
    # Plot the forecast
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['close'], label='Historical Prices')
    plt.plot(pd.date_range(start=df.index[-1], periods=8, closed='right'), forecast, label='Forecast', color='red')
    plt.xlabel('Date')
    plt.ylabel('Share Price')
    plt.title('ARIMA Forecast of Share Prices')
    plt.legend()
    ax: Axes = plt.gca()
    
    return forecast_list, ax