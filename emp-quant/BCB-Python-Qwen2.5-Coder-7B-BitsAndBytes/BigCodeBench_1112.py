
import csv
import random

# Constants
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}

def task_func(file_name="data.csv"):
    # Generate data for each hour of the current day
    data_rows = []
    for _ in range(24):
        row = {}
        for item in DATA:
            row[item] = random.randint(RANGE[item][0], RANGE[item][1])
        data_rows.append(row)

    # Write data to CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=DATA)
        writer.writeheader()
        writer.writerows(data_rows)

    return file_name