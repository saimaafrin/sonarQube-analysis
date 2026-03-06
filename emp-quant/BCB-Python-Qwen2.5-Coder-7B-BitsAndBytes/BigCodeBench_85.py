
import numpy as np
import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, random_seed=42):
    """
    Generates and plots weather data for a specified date range.

    Parameters:
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    random_seed (int): Seed for random number generation.

    Returns:
    DataFrame: A pandas DataFrame with columns ['Date', 'Temperature', 'Humidity', 'Wind Speed'].
    Axes: A matplotlib Axes object of the plot showing the generated weather data.
    """
    # Convert string dates to datetime objects
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)

    # Check if the end date is before the start date
    if end < start:
        raise ValueError("End date must be after start date.")

    # Set the random seed for reproducibility
    np.random.seed(random_seed)

    # Generate date range
    date_range = pd.date_range(start=start, end=end)

    # Generate random weather data
    temperatures = np.random.uniform(-10, 40, size=len(date_range))
    humidities = np.random.uniform(20, 100, size=len(date_range))
    wind_speeds = np.random.uniform(0, 20, size=len(date_range))

    # Create DataFrame
    weather_data = pd.DataFrame({
        'Date': date_range,
        'Temperature': temperatures,
        'Humidity': humidities,
        'Wind Speed': wind_speeds
    })

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature (°C)')
    ax.plot(weather_data['Date'], weather_data['Humidity'], label='Humidity (%)')
    ax.plot(weather_data['Date'], weather_data['Wind Speed'], label='Wind Speed (m/s)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Values')
    ax.set_title('Weather Data Over Time')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    return weather_data, ax