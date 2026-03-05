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

    # Define the path for the output CSV file
    output_file_path = os.path.join(output_dir, 'weather_data.csv')

    # Open the CSV file for writing
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Time', 'Condition'])

        # Generate weather data for the specified number of hours
        for _ in range(hours):
            # Write the current time and a random weather condition
            writer.writerow([current_time.strftime('%Y-%m-%d %H:%M:%S'), WEATHER_CONDITIONS[randint(0, 4)]])
            # Increment the time by one hour
            current_time += timedelta(hours=1)

    # Define the path for the backup directory
    backup_dir = os.path.join(output_dir, 'backup')

    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Define the path for the backup file
    backup_file_path = os.path.join(backup_dir, 'weather_data_backup.csv')

    # Copy the original file to the backup directory
    shutil.copy(output_file_path, backup_file_path)

    # Return the path of the generated CSV file
    return output_file_path