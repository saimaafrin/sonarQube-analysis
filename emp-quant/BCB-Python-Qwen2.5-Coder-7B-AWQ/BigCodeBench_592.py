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
        
        # Generate and write data for each hour
        for i in range(hours):
            current_time = datetime.now() + timedelta(hours=i)
            row = [current_time.strftime('%Y-%m-%d %H:%M:%S')]
            for sensor in SENSORS:
                if sensor == 'Temperature':
                    row.append(randint(20, 30))  # Random temperature between 20 and 30
                elif sensor == 'Humidity':
                    row.append(randint(40, 60))  # Random humidity between 40 and 60
                elif sensor == 'Pressure':
                    row.append(randint(1000, 1020))  # Random pressure between 1000 and 1020
            writer.writerow(row)

    # Return the number of hours processed
    return hours