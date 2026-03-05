
import csv
import os
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
# Constants
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Generate traffic data for different vehicle types
    data = {}
    for i in range(hours):
        for vehicle_type in VEHICLE_TYPES:
            data[vehicle_type] = randint(10, 100)
    # Save data to CSV file
    with open(os.path.join(output_dir, 'traffic_data.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Time', 'Car', 'Bus', 'Truck', 'Bike'])
        for i in range(hours):
            writer.writerow([i, data['Car'], data['Bus'], data['Truck'], data['Bike']])
    # Plot data
    df = pd.read_csv(os.path.join(output_dir, 'traffic_data.csv'))
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Vehicle Count'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Vehicle Count')
    ax.set_title('Traffic Data')
    plt.show()
    return (os.path.join(output_dir, 'traffic_data.csv'), fig)