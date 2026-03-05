
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Perform ARIMA forecasting
    model = ARIMA(df, order=(5, 1, 1))
    forecast = model.forecast(steps=7)

    # Create subplot
    fig, ax = plt.subplots()

    # Plot actual values
    ax.plot(df.index, df['Close'], label='Actual')

    # Plot forecasted values
    ax.plot(forecast.index, forecast['yhat'], label='Forecast')

    # Set x-axis labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Share Price')

    # Set title
    ax.set_title('ARIMA Forecast')

    # Add legend
    ax.legend()

    # Return forecasted prices and subplot
    return forecast['yhat'].tolist(), ax

# Load historical stock prices
df = pd.read_csv('stock_prices.csv', index_col='Date', parse_dates=['Date'])

# Perform ARIMA forecasting
forecast, ax = task_func(df)

# Print forecasted prices
print(forecast)

# Show subplot
plt.show()