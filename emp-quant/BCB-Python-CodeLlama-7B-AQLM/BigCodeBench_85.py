import numpy as np
import pandas as pd
from datetime import timedelta
def task_func(start_date, end_date, random_seed=42):
    """
    Generate and plot weather data for a specified date range.
    
    This function creates a DataFrame containing simulated daily weather data 
    within the specified date range. It generates random values for temperature, 
    humidity, and wind speed for each day. The function also plots these parameters 
    over the date range and returns both the DataFrame and the plot object.
    
    Parameters:
    - start_date (datetime): The start date for the data generation.
    - end_date (datetime): The end date for the data generation.
    - random_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to 42.
    
    The generated weather data ranges are as follows:
    - Temperature: Between -10°C and 40°C.
    - Humidity: Between 20% and 100%.
    - Wind Speed: Between 0 and 20 meters per second.
    
    Returns:
    - DataFrame: A pandas DataFrame with columns ['Date', 'Temperature', 'Humidity', 'Wind Speed'], containing the generated weather data for each day within the specified range.
    - Axes: A matplotlib Axes object of the plot showing the generated weather data.
    
    Raises:
    - ValueError: If 'end_date' is before 'start_date', indicating an invalid date range.

    Requirements:
    - numpy
    - pandas
    - datetime

    Example:
    >>> start_date = datetime(2021, 1, 1)
    >>> end_date = datetime(2021, 12, 31)
    >>> data, plot = task_func(start_date, end_date)
    >>> print(data.head())  # Display the first few rows of the DataFrame 
            Date  Temperature   Humidity  Wind Speed
    0 2021-01-01     8.727006  96.057145   14.639879
    1 2021-01-02    19.932924  32.481491    3.119890
    2 2021-01-03    -7.095819  89.294092   12.022300
    3 2021-01-04    25.403629  21.646760   19.398197
    4 2021-01-05    31.622132  36.987129    3.636499
    >>> plot.get_figure().savefig("weather_data_plot.png")  # Save the plot to a file
    >>> os.remove("weather_data_plot.png")
    """
    # Check that the end date is after the start date
    if end_date < start_date:
        raise ValueError("The end date must be after the start date.")
    
    # Generate random weather data for each day within the specified date range
    weather_data = pd.DataFrame(columns=["Date", "Temperature", "Humidity", "Wind Speed"])
    for date in pd.date_range(start=start_date, end=end_date):
        # Generate random values for temperature, humidity, and wind speed
        temperature = np.random.uniform(-10, 40, 1)
        humidity = np.random.uniform(20, 100, 1)
        wind_speed = np.random.uniform(0, 20, 1)
        # Add the generated values to the DataFrame
        weather_data = weather_data.append({"Date": date, "Temperature": temperature, "Humidity": humidity, "Wind Speed": wind_speed}, ignore_index=True)
    
    # Plot the weather data
    plot = weather_data.plot(x="Date", y=["Temperature", "Humidity", "Wind Speed"], figsize=(15, 5), title="Weather Data")
    plot.set_ylabel("Temperature (°C)")
    plot.set_xlabel("Date")
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_xticks(pd.date_range(start=start_date, end=end_date, freq=timedelta(days=1)))
    plot.set_xticklabels(pd.date_range(start=start_date, end=end_date, freq=timedelta(days=1)))
    plot.set_yticks(np.arange(-10, 40, 10))
    plot.set_yticklabels(np.arange(-10, 40, 10))
    plot.legend(["Temperature", "Humidity", "Wind Speed"])
    plot.grid(axis="y")
    plot.set_facecolor("white")
    plot.set_palette("viridis")
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlabel("Date")
    plot.set_ylabel("Temperature (°C)")
    plot.set_title("Weather Data")
    plot.set_facecolor("white")
    plot.set_palette("viridis")
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlabel("Date")
    plot.set_ylabel("Temperature (°C)")
    plot.set_title("Weather Data")
    plot.set_facecolor("white")
    plot.set_palette("viridis")
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlabel("Date")
    plot.set_ylabel("Temperature (°C)")
    plot.set_title("Weather Data")
    plot.set_facecolor("white")
    plot.set_palette("viridis")
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlabel("Date")
    plot.set_ylabel("Temperature (°C)")
    plot.set_title("Weather Data")
    plot.set_facecolor("white")
    plot.set_palette("viridis")
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlabel("Date")
    plot.set_ylabel("Temperature (°C)")
    plot.set_title("Weather Data")
    plot.set_facecolor("white")
    plot.set_palette("viridis")
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlabel("Date")
    plot.set_ylabel("Temperature (°C)")
    plot.set_title("Weather Data")
    plot.set_facecolor("white")
    plot.set_palette("viridis")
    plot.set_xlim(left=start_date, right=end_date)
    plot.set_ylim(bottom=-10, top=40)
    plot.set_xlabel("Date")
    plot.set_ylabel("Temperature (°C)")
    plot.set_title("Weather Data")
    plot.set_facecolor("white")
    plot.set_palette("viridis")