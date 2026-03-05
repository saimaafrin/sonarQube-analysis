
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

    # Generate the current time
    current_time = datetime.now()

    # Create the output file path
    output_file = os.path.join(output_dir, 'weather_data.csv')

    # Write the data to the CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Condition'])

        for _ in range(hours):
            writer.writerow([current_time.strftime('%Y-%m-%d %H:%M:%S'), WEATHER_CONDITIONS[randint(0, 4)]])
            current_time += timedelta(hours=1)

    # Backup the file to a backup directory
    backup_dir = os.path.join(output_dir, 'backup')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, 'weather_data_backup.csv')
    shutil.copy(output_file, backup_file)

    return output_file