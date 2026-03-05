
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

    # Define the file path
    file_path = os.path.join(output_dir, 'sensor_data.csv')

    # Open the CSV file for writing
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Time'] + SENSORS)

        # Generate data for the specified number of hours
        for i in range(hours * 60):
            # Calculate the current time
            current_time = datetime.now() + timedelta(minutes=i)
            # Generate random sensor data
            sensor_data = [randint(0, 100) for _ in range(len(SENSORS))]
            # Write the data to the CSV file
            writer.writerow([current_time.strftime('%Y-%m-%d %H:%M:%S')] + sensor_data)

    print(f"Sensor data saved to {file_path}")