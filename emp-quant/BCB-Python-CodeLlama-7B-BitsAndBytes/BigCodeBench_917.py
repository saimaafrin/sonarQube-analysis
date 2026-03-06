
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Create a new Axes object
    fig, ax = plt.subplots()

    # Plot the time series data
    ax.plot(df['Close'])

    # Fit an ARIMA model to the data
    model = ARIMA(df['Close'], order=(1, 1, 1))
    results = model.fit()

    # Forecast the next 7 days
    forecast = results.forecast(steps=7)

    # Plot the forecast
    ax.plot(forecast)

    # Return the forecast and the Axes object
    return forecast, ax

# Load the data
df = pd.read_csv('data.csv')

# Call the function
forecast, ax = task_func(df)

# Plot the forecast
ax.set_title('Forecasted Closing Prices')
ax.set_xlabel('Date')
ax.set_ylabel('Closing Price')
ax.legend()
plt.show()