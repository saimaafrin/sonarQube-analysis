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
    # Create a CSV file with the specified number of hours
    csv_file = f'weather_data_{hours}.csv'
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Condition'])
        for i in range(hours):
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            condition = WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS) - 1)]
            writer.writerow([time, condition])

    # Back up the CSV file to the backup directory
    backup_file = f'{output_dir}/{csv_file}'
    shutil.copy(csv_file, backup_file)

    # Return the path of the generated CSV file
    return csv_file
hours = 8
output_dir = './output'