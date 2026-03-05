
import csv
import os
import shutil
from datetime import datetime
from random import randint
# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Generate weather data
    weather_data = []
    for i in range(hours):
        time = datetime.now() + timedelta(hours=i)
        condition = WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS) - 1)]
        weather_data.append([time, condition])
    # Save to CSV file
    csv_file = os.path.join(output_dir, 'weather_data.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(weather_data)
    # Backup CSV file
    backup_file = os.path.join(output_dir, 'weather_data_backup.csv')
    shutil.copyfile(csv_file, backup_file)
    return csv_file