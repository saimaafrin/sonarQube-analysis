
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
    data = []
    for hour in range(hours):
        time = datetime.now() + timedelta(hours=hour)
        vehicle_counts = {vehicle: randint(10, 100) for vehicle in VEHICLE_TYPES}
        data.append([time, *vehicle_counts.values()])

    # Save data to CSV
    csv_file_path = os.path.join(output_dir, 'traffic_data.csv')
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time'] + VEHICLE_TYPES)
        writer.writerows(data)

    # Plot the data
    df = pd.read_csv(csv_file_path)
    df['Time'] = pd.to_datetime(df['Time'])
    df.set_index('Time', inplace=True)
    ax = df.plot(kind='line', title='Traffic Data Over Time', ylabel='Vehicle Count')
    ax.set_xlabel('Time')

    return csv_file_path, ax