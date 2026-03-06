
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
    # Generate traffic data for different vehicle types over the specified number of hours
    data = {}
    for vehicle_type in VEHICLE_TYPES:
        data[vehicle_type] = []
        for i in range(hours):
            data[vehicle_type].append(randint(0, 100))

    # Save the data to a CSV file
    csv_file = os.path.join(output_dir, 'traffic_data.csv')
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Time', 'Car', 'Bus', 'Truck', 'Bike'])
        for i in range(hours):
            writer.writerow([i, data['Car'][i], data['Bus'][i], data['Truck'][i], data['Bike'][i]])

    # Plot the data in a line chart
    fig, ax = plt.subplots()
    ax.plot(data['Car'], label='Car')
    ax.plot(data['Bus'], label='Bus')
    ax.plot(data['Truck'], label='Truck')
    ax.plot(data['Bike'], label='Bike')
    ax.set_xlabel('Time')
    ax.set_ylabel('Vehicle Count')
    ax.legend()
    plt.show()

    return csv_file, ax

# Call the function with the specified number of hours
csv_file, ax = task_func(10)