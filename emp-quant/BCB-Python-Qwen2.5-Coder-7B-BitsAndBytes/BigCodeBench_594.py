
import csv
import os
import shutil
from datetime import datetime, timedelta
from random import choice

# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate the current time
    start_time = datetime.now()

    # Create a list to hold the weather data
    weather_data = []

    # Populate the weather data for the specified number of hours
    for _ in range(hours):
        current_time = start_time + timedelta(hours=_)
        condition = choice(WEATHER_CONDITIONS)
        weather_data.append([current_time.strftime('%Y-%m-%d %H:%M:%S'), condition])

    # Define the output file path
    output_file_path = os.path.join(output_dir, f'weather_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv')

    # Write the weather data to a CSV file
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Condition'])
        writer.writerows(weather_data)

    # Backup the file to a backup directory
    backup_dir = './backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup_file_path = os.path.join(backup_dir, os.path.basename(output_file_path))
    shutil.copy2(output_file_path, backup_file_path)

    return output_file_path