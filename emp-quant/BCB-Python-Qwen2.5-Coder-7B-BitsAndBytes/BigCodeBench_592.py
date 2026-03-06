
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

    # Define the filename
    filename = os.path.join(output_dir, f'sensor_data_{hours}h.csv')

    # Open the CSV file for writing
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Time'] + SENSORS)
        
        # Generate and write the data rows
        current_time = datetime.now()
        for _ in range(hours * 60):  # Each minute of data
            row = [current_time]
            for sensor in SENSORS:
                value = randint(0, 100)  # Random values between 0 and 100
                row.append(value)
            writer.writerow(row)
            current_time += timedelta(minutes=1)

    print(f'Data saved to {filename}')