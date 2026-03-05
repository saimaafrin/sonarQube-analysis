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
    csv_file = os.path.join(output_dir, 'sensor_data.csv')
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Temperature', 'Humidity', 'Pressure'])

        # Generate data for the specified number of hours
        for i in range(hours):
            # Generate random data for each sensor
            temperature = randint(10, 30)
            humidity = randint(10, 90)
            pressure = randint(900, 1100)

            # Write data to CSV file
            writer.writerow([datetime.now(), temperature, humidity, pressure])