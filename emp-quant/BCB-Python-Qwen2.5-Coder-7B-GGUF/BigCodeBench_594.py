
import csv
import os
import shutil
from datetime import datetime, timedelta
from random import randint
# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define backup directory
    backup_dir = os.path.join(output_dir, 'backup')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Generate weather data
    current_time = datetime.now()
    weather_data = []
    for _ in range(hours):
        condition = WEATHER_CONDITIONS[randint(0, 4)]
        weather_data.append([current_time.strftime('%Y-%m-%d %H:%M:%S'), condition])
        current_time += timedelta(hours=1)
    
    # Save data to CSV file
    csv_file_path = os.path.join(output_dir, f'weather_data_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv')
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time', 'Condition'])
        writer.writerows(weather_data)
    
    # Backup the CSV file
    shutil.copy(csv_file_path, backup_dir)
    
    return csv_file_path