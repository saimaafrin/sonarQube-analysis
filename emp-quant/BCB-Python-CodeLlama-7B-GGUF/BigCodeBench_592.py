
import csv
import os
from datetime import datetime
from random import randint
# Constants
SENSORS = ['Temperature', 'Humidity', 'Pressure']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Generate data for the specified number of hours
    for i in range(hours):
        # Create a new CSV file for each hour
        with open(os.path.join(output_dir, f'{i}.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write column headers
            writer.writerow(['Time', 'Temperature', 'Humidity', 'Pressure'])
            # Generate random data for each sensor
            for sensor in SENSORS:
                writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), randint(10, 30), randint(10, 90), randint(900, 1100)])