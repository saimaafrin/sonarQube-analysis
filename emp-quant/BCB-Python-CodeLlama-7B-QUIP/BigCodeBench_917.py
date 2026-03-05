
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Tuple

def task_func(df: pd.DataFrame) -> Tuple[List[float], Axes]:
    # Load the data
    df = df.dropna()

    # Create the ARIMA model
    model = ARIMA(df, order=(1, 1, 1))

    # Forecast the next 7 days
    forecasts = model.forecast(7)

    # Convert the forecasts to a list
    forecasts_list = forecasts.values.tolist()

    # Plot the forecasts
    fig, ax = plt.subplots()
    ax.plot(forecasts_list)
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    ax.set_title("Forecasted Closing Prices")
    ax.grid(True)

    return forecasts_list, fig