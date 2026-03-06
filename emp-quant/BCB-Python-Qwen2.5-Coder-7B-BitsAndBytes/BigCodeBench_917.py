
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Ensure the DataFrame has a datetime index
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # Fit an ARIMA model to the data
    model = ARIMA(df['close'], order=(5,1,0))  # Example order, adjust as needed
    model_fit = model.fit()
    
    # Forecast the next 7 days
    forecast = model_fit.forecast(steps=7)
    forecast_list = forecast.tolist()
    
    # Plotting the original data and the forecast
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['close'], label='Historical Close Prices')
    ax.plot(pd.date_range(start=df.index[-1], periods=8)[1:], forecast, label='Forecasted Close Prices', color='red')
    ax.legend()
    ax.set_title('ARIMA Forecast of Share Closing Prices')
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    
    return forecast_list, ax