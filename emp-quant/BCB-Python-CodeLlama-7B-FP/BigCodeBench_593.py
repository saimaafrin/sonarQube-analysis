import csv
import os
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Generate traffic data for different vehicle types over a specified number of hours
    data = {}
    for vehicle_type in VEHICLE_TYPES:
        data[vehicle_type] = []
        for i in range(hours):
            data[vehicle_type].append(randint(0, 100))
    # Save the data to a CSV file with columns 'Time', 'Car', 'Bus', 'Truck', and 'Bike'
    with open(os.path.join(output_dir, 'traffic_data.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Time'] + VEHICLE_TYPES)
        for i in range(hours):
            writer.writerow([i] + [data[vehicle_type][i] for vehicle_type in VEHICLE_TYPES])
    # Plot the data in a line chart with 'Time' on x-axis and 'Vehicle Count' on y-axis
    fig, ax = plt.subplots()
    ax.plot(data['Car'], label='Car')
    ax.plot(data['Bus'], label='Bus')
    ax.plot(data['Truck'], label='Truck')
    ax.plot(data['Bike'], label='Bike')
    ax.set_xlabel('Time')
    ax.set_ylabel('Vehicle Count')
    ax.legend()
    plt.show()
    return os.path.join(output_dir, 'traffic_data.csv'), ax