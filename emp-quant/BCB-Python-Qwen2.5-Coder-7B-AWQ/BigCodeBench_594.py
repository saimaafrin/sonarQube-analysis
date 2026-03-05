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

    # Generate the path for the CSV file
    csv_file_path = os.path.join(output_dir, f'weather_data_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv')

    # Generate weather data
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Condition'])
        for i in range(hours):
            current_time = datetime.now() + timedelta(hours=i)
            condition = WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS) - 1)]
            writer.writerow([current_time.strftime('%Y-%m-%d %H:%M:%S'), condition])

    # Backup the file to a backup directory
    backup_dir = os.path.join(output_dir, 'backup')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup_file_path = os.path.join(backup_dir, os.path.basename(csv_file_path))
    shutil.copy2(csv_file_path, backup_file_path)

    return csv_file_path