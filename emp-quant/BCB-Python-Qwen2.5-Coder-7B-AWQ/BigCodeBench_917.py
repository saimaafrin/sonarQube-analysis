import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple
def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Ensure the DataFrame has a datetime index
    df.set_index('date', inplace=True)
    
    # Fit the ARIMA model
    model = ARIMA(df['close'], order=(5,1,0))
    model_fit = model.fit()
    
    # Forecast the next 7 days
    forecast = model_fit.forecast(steps=7)
    
    # Plot the forecast
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['close'], label='Historical Prices')
    plt.plot(pd.date_range(start=df.index[-1], periods=8, closed='right'), forecast, label='Forecasted Prices', color='red')
    plt.legend()
    plt.title('ARIMA Forecast of Share Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    
    # Return the forecasted prices and the Axes object
    return forecast.tolist(), plt.gca()