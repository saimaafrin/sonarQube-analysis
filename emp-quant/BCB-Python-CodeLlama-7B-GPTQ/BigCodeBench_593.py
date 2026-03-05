import csv
import os
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'
def task_func(hours, output_dir=OUTPUT_DIR):
    # Generate traffic data
    data = []
    for i in range(hours):
        for vehicle_type in VEHICLE_TYPES:
            data.append({
                'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Vehicle Type': vehicle_type,
                'Count': randint(0, 100)
            })

    # Save data to CSV file
    csv_file = os.path.join(output_dir, f'traffic_data_{hours}.csv')
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Time', 'Vehicle Type', 'Count'])
        writer.writeheader()
        writer.writerows(data)

    # Plot data
    df = pd.read_csv(csv_file)
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Count'], label=f'Vehicle Count ({hours} hours)')
    ax.set_xlabel('Time')
    ax.set_ylabel('Vehicle Count')
    ax.legend()
    plt.show()

    return csv_file, ax