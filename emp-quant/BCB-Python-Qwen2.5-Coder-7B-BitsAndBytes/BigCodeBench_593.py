
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
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate traffic data
    data = {'Time': [], 'Car': [], 'Bus': [], 'Truck': [], 'Bike': []}
    current_time = datetime.now()
    for _ in range(hours * 60):  # Assuming one data point every minute
        data['Time'].append(current_time)
        for vehicle_type in VEHICLE_TYPES:
            data[vehicle_type].append(randint(10, 50))  # Random count between 10 and 50
        current_time += timedelta(minutes=1)

    # Save data to CSV
    csv_file_path = os.path.join(output_dir, f'traffic_data_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv')
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)

    # Plot the data
    fig, ax = plt.subplots()
    for vehicle_type in VEHICLE_TYPES:
        ax.plot(df['Time'], df[vehicle_type], label=vehicle_type)
    ax.set_xlabel('Time')
    ax.set_ylabel('Vehicle Count')
    ax.set_title('Traffic Data Over Time')
    ax.legend()

    return csv_file_path, ax