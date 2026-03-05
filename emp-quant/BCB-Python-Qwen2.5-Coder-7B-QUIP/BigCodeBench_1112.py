
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
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(DATA)
        for _ in range(24):  # 24 hours in a day
            row = [
                random.uniform(RANGE['Temperature'][0], RANGE['Temperature'][1]),
                random.uniform(RANGE['Humidity'][0], RANGE['Humidity'][1]),
                random.uniform(RANGE['Pressure'][0], RANGE['Pressure'][1])
            ]
            writer.writerow(row)
    return file_name