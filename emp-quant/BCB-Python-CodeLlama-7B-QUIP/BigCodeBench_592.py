
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
    # Create a CSV file for each sensor
    for sensor in SENSORS:
        with open(os.path.join(output_dir, f'{sensor}.csv'), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header row
            writer.writerow(['Time', 'Temperature', 'Humidity', 'Pressure'])
            # Generate data for the specified number of hours
            for i in range(hours):
                # Generate random values for the three sensors
                temperature = randint(20, 30)
                humidity = randint(40, 60)
                pressure = randint(1000, 1100)
                # Write the data to the CSV file
                writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity, pressure])
    print(f'Sensor data generated for {hours} hours')