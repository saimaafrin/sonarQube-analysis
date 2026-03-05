
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
        weather_data.append({
            'Time': datetime.now().strftime('%H:%M:%S'),
            'Condition': WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS) - 1)]
        })
    # Write to CSV file
    with open(os.path.join(output_dir, 'weather.csv'), 'w') as f:
        writer = csv.DictWriter(f, ['Time', 'Condition'])
        writer.writeheader()
        for data in weather_data:
            writer.writerow(data)
    # Backup file
    shutil.copy(os.path.join(output_dir, 'weather.csv'), os.path.join(output_dir, 'weather.csv.bak'))
    return os.path.join(output_dir, 'weather.csv')