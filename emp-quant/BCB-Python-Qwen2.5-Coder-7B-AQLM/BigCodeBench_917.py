
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Ensure the DataFrame has a datetime index
    df.set_index('date', inplace=True)
    
    # Fit the ARIMA model
    model = ARIMA(df['price'], order=(5,1,0))
    model_fit = model.fit()
    
    # Forecast the next 7 days
    forecast = model_fit.forecast(steps=7)
    forecast_list = forecast.tolist()
    
    # Plot the forecast
    fig, ax = plt.subplots()
    ax.plot(df.index, df['price'], label='Historical Prices')
    ax.plot(pd.date_range(start=df.index[-1], periods=8, closed='right'), forecast_list, label='Forecasted Prices', linestyle='--')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('ARIMA Forecast for Next 7 Days')
    ax.legend()
    
    return forecast_list, ax