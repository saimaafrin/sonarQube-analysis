
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

def task_func(start_date, end_date, random_seed=42):
    if end_date < start_date:
        raise ValueError("'end_date' is before 'start_date'")

    # Generate random weather data for each day within the specified range
    date_range = pd.date_range(start_date, end_date)
    temperature = np.random.uniform(-10, 40, size=len(date_range))
    humidity = np.random.uniform(20, 100, size=len(date_range))
    wind_speed = np.random.uniform(0, 20, size=len(date_range))

    # Create a DataFrame with the generated weather data
    weather_data = pd.DataFrame({
        'Date': date_range,
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind Speed': wind_speed
    })

    # Plot the weather data
    fig, ax = plt.subplots()
    ax.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature')
    ax.plot(weather_data['Date'], weather_data['Humidity'], label='Humidity')
    ax.plot(weather_data['Date'], weather_data['Wind Speed'], label='Wind Speed')
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.legend()

    return weather_data, fig