import csv
import os
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    """
    Generates traffic data for different vehicle types over a specified number of hours,
    saves the data to a CSV file with coloumns 'Time', 'Car', 'Bus', 'Truck', and 'Bike',
    and plots the data in a line chart with 'Time' on x-axis and 'Vehicle Count' on y-axis.

    Parameters:
    - hours (int): Number of hours to generate data for.
    - output_dir (str, optional): The output file path

    Returns:
    - tuple: Path to the CSV file and the matplotlib axes object of the line plot.

    Requirements:
    - pandas
    - os
    - csv
    - matplotlib.pyplot
    - random
    - datetime

    Example:
    >>> import matplotlib
    >>> file_path, ax = task_func(2)  # Generate data for 2 hours
    >>> isinstance(file_path, str)
    True
    >>> 'traffic_data.csv' in file_path
    True
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Create a list of vehicle counts for each vehicle type
    vehicle_counts = [0] * len(VEHICLE_TYPES)

    # Generate data for each hour
    for hour in range(hours):
        # Generate a random number of vehicles for each vehicle type
        for i in range(len(VEHICLE_TYPES)):
            vehicle_counts[i] += randint(0, 10)

        # Create a list of time stamps for each hour
        time_stamps = [datetime.now() + datetime.timedelta(hours=hour)] * len(VEHICLE_TYPES)

        # Create a list of vehicle counts for each hour
        vehicle_counts_hour = [vehicle_counts[i] for i in range(len(VEHICLE_TYPES))]

        # Create a list of vehicle types for each hour
        vehicle_types = [VEHICLE_TYPES[i] for i in range(len(VEHICLE_TYPES))]

        # Create a list of lists containing the data for each hour
        data = [time_stamps, vehicle_types, vehicle_counts_hour]

        # Create a dataframe from the data
        df = pd.DataFrame(data, columns=['Time', 'Vehicle Type', 'Vehicle Count'])

        # Save the dataframe to a CSV file
        file_path = os.path.join(output_dir, 'traffic_data.csv')
        df.to_csv(file_path, index=False)

        # Plot the data
        fig, ax = plt.subplots()
        ax.plot(df['Time'], df['Vehicle Count'], label=df['Vehicle Type'])
        ax.set_xlabel('Time')
        ax.set_ylabel('Vehicle Count')
        ax.set_title('Traffic Data')
        ax.legend()

    return file_path, ax