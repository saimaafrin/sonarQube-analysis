import numpy as np
import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
def task_func(start_date, end_date, random_seed=42):
    """
    Generate and plot weather data for a specified date range.

    Parameters
    ----------
    start_date : str
        Start date of the date range.
    end_date : str
        End date of the date range.
    random_seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    DataFrame
        A pandas DataFrame with columns ['Date', 'Temperature', 'Humidity', 'Wind Speed'], containing the generated weather data for each day within the specified range.
    Axes
        A matplotlib Axes object of the plot showing the generated weather data.

    Raises
    ------
    ValueError
        If 'end_date' is before 'start_date', indicating an invalid date range.
    """
    if end_date < start_date:
        raise ValueError("'end_date' must be after 'start_date'")

    # Generate random weather data for each day within the specified date range
    date_range = pd.date_range(start_date, end_date)
    temperature = np.random.uniform(-10, 40, size=len(date_range))
    humidity = np.random.uniform(20, 100, size=len(date_range))
    wind_speed = np.random.uniform(0, 20, size=len(date_range))

    # Create a DataFrame with the generated weather data
    weather_data = pd.DataFrame({
        "Date": date_range,
        "Temperature": temperature,
        "Humidity": humidity,
        "Wind Speed": wind_speed
    })

    # Plot the generated weather data
    fig, ax = plt.subplots()
    ax.plot(weather_data["Date"], weather_data["Temperature"], label="Temperature")
    ax.plot(weather_data["Date"], weather_data["Humidity"], label="Humidity")
    ax.plot(weather_data["Date"], weather_data["Wind Speed"], label="Wind Speed")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Weather Data")
    ax.legend()

    return weather_data, ax
start_date = "2022-01-01"
end_date = "2022-01-31"