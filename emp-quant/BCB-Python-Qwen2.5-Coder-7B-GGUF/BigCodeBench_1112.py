
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
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(DATA)
        for _ in range(24 * 60):  # 24 hours * 60 minutes
            row = [random.randint(RANGE[col][0], RANGE[col][1]) for col in DATA]
            writer.writerow(row)
    return file_name