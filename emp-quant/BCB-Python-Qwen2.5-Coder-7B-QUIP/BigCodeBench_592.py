
import csv
import os
from datetime import datetime, timedelta
from random import randint
# Constants
SENSORS = ['Temperature', 'Humidity', 'Pressure']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the output file path
    output_file = os.path.join(output_dir, 'sensor_data.csv')

    # Open the file for writing
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header
        writer.writerow(['Time', 'Temperature', 'Humidity', 'Pressure'])

        # Generate data for the specified number of hours
        for _ in range(hours * 60):
            # Generate a random time within the current hour
            current_time = datetime.now() + timedelta(minutes=_)
            # Generate random sensor data
            sensor_data = [current_time.strftime('%Y-%m-%d %H:%M:%S')] + [randint(0, 100) for _ in range(3)]
            # Write the data to the CSV file
            writer.writerow(sensor_data)

    print(f"Data saved to {output_file}")