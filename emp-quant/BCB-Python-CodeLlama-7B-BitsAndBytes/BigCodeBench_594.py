
import csv
import os
import shutil
from datetime import datetime
from random import randint

# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate weather data for the specified number of hours
    for i in range(hours):
        # Generate a random time
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Generate a random weather condition
        condition = WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS) - 1)]

        # Write the data to a CSV file
        with open(os.path.join(output_dir, f'weather_{i}.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([time, condition])

    # Back up the CSV file to a backup directory
    shutil.copy(os.path.join(output_dir, f'weather_{i}.csv'), os.path.join(output_dir, 'backup', f'weather_{i}.csv'))

    # Return the path of the generated CSV file
    return os.path.join(output_dir, f'weather_{i}.csv')

# Call the function with the desired number of hours
path = task_func(10)
print(path)