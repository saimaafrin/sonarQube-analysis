
import csv
import os
import shutil
from datetime import datetime, timedelta
from random import randint
# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate the CSV file path
    output_file = os.path.join(output_dir, 'weather_data.csv')

    # Open the CSV file for writing
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Condition'])

        # Generate weather data for the specified number of hours
        for _ in range(hours):
            # Generate a random time within the current hour
            current_time = datetime.now() + timedelta(seconds=randint(0, 3599))
            # Generate a random weather condition
            condition = WEATHER_CONDITIONS[randint(0, 4)]
            # Write the data to the CSV file
            writer.writerow([current_time, condition])

    # Backup the file to the backup directory
    backup_dir = './backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup_file = os.path.join(backup_dir, 'weather_data_backup.csv')
    shutil.copy(output_file, backup_file)

    # Return the path of the generated CSV file
    return output_file