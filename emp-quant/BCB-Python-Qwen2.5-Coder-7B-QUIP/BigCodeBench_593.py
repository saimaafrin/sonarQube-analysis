
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
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate traffic data
    data = []
    for hour in range(hours):
        row = {'Time': hour}
        for vehicle_type in VEHICLE_TYPES:
            row[vehicle_type] = randint(1, 100)  # Random count between 1 and 100
        data.append(row)

    # Save data to CSV
    csv_file_path = os.path.join(output_dir, 'traffic_data.csv')
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Time'] + VEHICLE_TYPES)
        writer.writeheader()
        writer.writerows(data)

    # Plot the data
    df = pd.DataFrame(data)
    df.set_index('Time', inplace=True)
    fig, ax = plt.subplots()
    df.plot(ax=ax, legend=True)
    ax.set_xlabel('Time (hours)')
    ax.set_ylabel('Vehicle Count')
    ax.set_title('Traffic Data')

    # Show the plot
    plt.show()

    # Return the path to the CSV file and the axes object
    return csv_file_path, ax