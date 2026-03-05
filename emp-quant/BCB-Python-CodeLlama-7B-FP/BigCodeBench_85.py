import numpy as np
import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
def task_func(start_date, end_date, random_seed=42):
    """
    Generate and plot weather data for a specified date range.

    Parameters
    ----------
    start_date : datetime.date
        The start date of the date range.
    end_date : datetime.date
        The end date of the date range.
    random_seed : int, optional
        The random seed to use for generating random numbers.

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

    # Generate random weather data for each day within the specified range
    num_days = (end_date - start_date).days
    temperature = np.random.uniform(-10, 40, num_days)
    humidity = np.random.uniform(20, 100, num_days)
    wind_speed = np.random.uniform(0, 20, num_days)

    # Create a DataFrame with the generated weather data
    df = pd.DataFrame({
        "Date": pd.date_range(start_date, end_date),
        "Temperature": temperature,
        "Humidity": humidity,
        "Wind Speed": wind_speed
    })

    # Plot the generated weather data
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Temperature"], label="Temperature")
    ax.plot(df["Date"], df["Humidity"], label="Humidity")
    ax.plot(df["Date"], df["Wind Speed"], label="Wind Speed")
    ax.set_xlabel("Date")
    ax.set_ylabel("Weather Data")
    ax.legend()

    return df, ax
start_date = pd.to_datetime("2022-01-01")
end_date = pd.to_datetime("2022-01-31")