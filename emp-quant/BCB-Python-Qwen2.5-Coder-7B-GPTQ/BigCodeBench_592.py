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
            data_row = [current_time.strftime('%Y-%m-%d %H:%M:%S')]
            for sensor in SENSORS:
                # Generate random data for each sensor
                if sensor == 'Temperature':
                    data_row.append(randint(20, 35))  # Temperature between 20°C and 35°C
                elif sensor == 'Humidity':
                    data_row.append(randint(30, 60))  # Humidity between 30% and 60%
                elif sensor == 'Pressure':
                    data_row.append(randint(1000, 1050))  # Pressure between 1000 hPa and 1050 hPa
            writer.writerow(data_row)

    return hours