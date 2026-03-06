
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

    # Create CSV file for each sensor
    for sensor in SENSORS:
        csv_file = os.path.join(output_dir, f'{sensor}.csv')
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Time', 'Value'])

            # Generate data for the specified number of hours
            for i in range(hours):
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                value = randint(0, 100)
                writer.writerow([time, value])

    print(f'Data generated for {hours} hours and saved to {output_dir}')

# Call the function with the desired number of hours
task_func(10)