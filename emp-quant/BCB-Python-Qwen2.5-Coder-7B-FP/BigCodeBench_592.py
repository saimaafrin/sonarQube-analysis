import csv
import os
from datetime import datetime, timedelta
from random import randint
SENSORS = ['Temperature', 'Humidity', 'Pressure']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define the output file path
    output_file = os.path.join(output_dir, 'sensor_data.csv')

    # Open the CSV file for writing
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Time'] + SENSORS)
        
        # Generate and write data for the specified number of hours
        for i in range(hours):
            current_time = datetime.now() + timedelta(hours=i)
            row = [current_time.strftime('%Y-%m-%d %H:%M:%S')]
            for sensor in SENSORS:
                # Generate random values for each sensor
                if sensor == 'Temperature':
                    value = randint(20, 35)  # Temperature in Celsius
                elif sensor == 'Humidity':
                    value = randint(30, 60)  # Humidity in percentage
                elif sensor == 'Pressure':
                    value = randint(1000, 1020)  # Pressure in hPa
                row.append(value)
            writer.writerow(row)

    return hours