import numpy as np
import pandas as pd
from datetime import timedelta
def task_func(start_date, end_date, random_seed=42):
    """
    Generates and plots weather data for a specified date range.
    
    Parameters:
    - start_date (str): The start date in 'YYYY-MM-DD' format.
    - end_date (str): The end date in 'YYYY-MM-DD' format.
    - random_seed (int): The seed for the random number generator for reproducibility.
    
    Returns:
    - DataFrame: A pandas DataFrame with columns ['Date', 'Temperature', 'Humidity', 'Wind Speed'].
    - Axes: A matplotlib Axes object of the plot showing the generated weather data.
    """
    # Validate date range
    if pd.to_datetime(end_date) < pd.to_datetime(start_date):
        raise ValueError("End date must be after start date.")
    
    # Set random seed for reproducibility
    np.random.seed(random_seed)
    
    # Generate date range
    date_range = pd.date_range(start=start_date, end=end_date)
    
    # Generate random weather data
    temperature = np.random.uniform(-10, 40, size=len(date_range))
    humidity = np.random.uniform(20, 100, size=len(date_range))
    wind_speed = np.random.uniform(0, 20, size=len(date_range))
    
    # Create DataFrame
    weather_data = pd.DataFrame({
        'Date': date_range,
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind Speed': wind_speed
    })
    
    # Plot the data
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(weather_data['Date'], weather_data['Temperature'], label='Temperature (°C)')
    ax.plot(weather_data['Date'], weather_data['Humidity'], label='Humidity (%)')
    ax.plot(weather_data['Date'], weather_data['Wind Speed'], label='Wind Speed (m/s)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Values')
    ax.set_title('Weather Data Over Time')
    ax.legend()
    
    return weather_data, ax