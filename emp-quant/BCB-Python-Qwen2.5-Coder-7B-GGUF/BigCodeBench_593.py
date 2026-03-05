
import csv
import os
from datetime import datetime, timedelta
from random import randint
import matplotlib.pyplot as plt
import pandas as pd

# Constants
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate traffic data
    data = {'Time': [], 'Car': [], 'Bus': [], 'Truck': [], 'Bike': []}
    current_time = datetime.now()
    for _ in range(hours * 60):
        data['Time'].append(current_time)
        for vehicle in VEHICLE_TYPES:
            data[vehicle].append(randint(0, 100))  # Random count between 0 and 100
        current_time += timedelta(minutes=1)

    # Save data to CSV
    csv_file_path = os.path.join(output_dir, 'traffic_data.csv')
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerows(data)

    # Plot the data
    df = pd.DataFrame(data)
    df.set_index('Time', inplace=True)
    ax = df.plot(kind='line', figsize=(10, 6))
    ax.set_xlabel('Time')
    ax.set_ylabel('Vehicle Count')
    ax.set_title('Traffic Data Over Time')

    return csv_file_path, ax