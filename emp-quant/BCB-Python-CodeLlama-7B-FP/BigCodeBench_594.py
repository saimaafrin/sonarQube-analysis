import csv
import os
import shutil
from datetime import datetime
from random import randint
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    """
    Generate weather data for the specified number of hours, save it in a CSV file with columns 'Time' and 'Condition', and back up the file to a backup directory.
    """
    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate weather data
    weather_data = []
    for i in range(hours):
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        condition = WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS) - 1)]
        weather_data.append([time, condition])

    # Save weather data to CSV file
    csv_file = os.path.join(output_dir, 'weather_data.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(weather_data)

    # Back up CSV file to backup directory
    backup_dir = os.path.join(output_dir, 'backup')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    shutil.copy(csv_file, os.path.join(backup_dir, 'weather_data.csv'))

    return csv_file