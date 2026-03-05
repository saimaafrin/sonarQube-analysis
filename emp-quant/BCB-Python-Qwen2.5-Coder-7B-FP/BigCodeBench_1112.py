import csv
import random
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}
def task_func(file_name="data.csv"):
    # Generate data for each hour of the day
    data_points = []
    for hour in range(24):
        row = {}
        for item in DATA:
            row[item] = random.randint(RANGE[item][0], RANGE[item][1])
        data_points.append(row)
    
    # Write data to CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=DATA)
        writer.writeheader()
        for row in data_points:
            writer.writerow(row)
    
    return file_name