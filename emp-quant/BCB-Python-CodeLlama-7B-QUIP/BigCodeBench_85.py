
import numpy as np
import pandas as pd
from datetime import timedelta

def task_func(start_date, end_date, random_seed=42):
    if start_date > end_date:
        raise ValueError("Invalid date range")

    # Generate random values for temperature, humidity, and wind speed
    temperature = np.random.uniform(-10, 40, size=end_date - start_date)
    humidity = np.random.uniform(20, 100, size=end_date - start_date)
    wind_speed = np.random.uniform(0, 20, size=end_date - start_date)

    # Create a DataFrame with the generated data
    df = pd.DataFrame({
        "Date": [start_date + timedelta(i) for i in range(end_date - start_date)],
        "Temperature": temperature,
        "Humidity": humidity,
        "Wind Speed": wind_speed
    })

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Temperature"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature")
    ax.set_title("Weather Data")

    return df, fig