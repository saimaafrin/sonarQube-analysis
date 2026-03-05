import csv
import os
from datetime import datetime
from random import randint
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    """
    Generate sensor data for the specified number of hours and save it in a CSV file with columns 'Time', 'Temperature', 'Humidity', and 'Pressure'.
    """
    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create CSV file
    csv_file = os.path.join(output_dir, f'data_{hours}.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Temperature', 'Humidity', 'Pressure'])

        # Generate data for the specified number of hours
        for i in range(hours):
            # Generate random values for temperature, humidity, and pressure
            temperature = randint(10, 30)
            humidity = randint(10, 90)
            pressure = randint(900, 1000)

            # Write data to CSV file
            writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity, pressure])

    print(f'Data generated and saved to {csv_file}')
hours = 24