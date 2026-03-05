
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta

def task_func(start_date, end_date, random_seed=42):
    if end_date < start_date:
        raise ValueError("'end_date' must be after 'start_date'")

    # Generate random weather data for each day within the specified range
    np.random.seed(random_seed)
    weather_data = pd.DataFrame(
        index=pd.date_range(start_date, end_date),
        columns=['Temperature', 'Humidity', 'Wind Speed']
    )
    weather_data['Temperature'] = np.random.uniform(-10, 40, size=len(weather_data))
    weather_data['Humidity'] = np.random.uniform(20, 100, size=len(weather_data))
    weather_data['Wind Speed'] = np.random.uniform(0, 20, size=len(weather_data))

    # Plot the weather data
    fig, ax = plt.subplots()
    ax.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature')
    ax.plot(weather_data['Date'], weather_data['Humidity'], label='Humidity')
    ax.plot(weather_data['Date'], weather_data['Wind Speed'], label='Wind Speed')
    ax.set_xlabel('Date')
    ax.set_ylabel('Weather Parameter')
    ax.set_title('Weather Data for {} to {}'.format(start_date, end_date))
    ax.legend()

    return weather_data, ax