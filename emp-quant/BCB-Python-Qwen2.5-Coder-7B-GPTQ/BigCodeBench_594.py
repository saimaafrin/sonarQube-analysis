import csv
import os
import shutil
from datetime import datetime, timedelta
from random import randint
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate the current time
    current_time = datetime.now()

    # Create a list to store the weather data
    weather_data = []

    # Generate weather data for the specified number of hours
    for _ in range(hours):
        # Generate a random weather condition
        condition = WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS) - 1)]
        # Append the time and condition to the weather data list
        weather_data.append([current_time, condition])
        # Increment the time by one hour
        current_time += timedelta(hours=1)

    # Define the path of the generated CSV file
    csv_file_path = os.path.join(output_dir, 'weather_data.csv')

    # Write the weather data to a CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Condition'])  # Write the header
        writer.writerows(weather_data)  # Write the data

    # Define the path of the backup directory
    backup_dir = os.path.join(output_dir, 'backup')

    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Backup the CSV file to the backup directory
    backup_file_path = os.path.join(backup_dir, 'weather_data.csv')
    shutil.copy(csv_file_path, backup_file_path)

    # Return the path of the generated CSV file
    return csv_file_path