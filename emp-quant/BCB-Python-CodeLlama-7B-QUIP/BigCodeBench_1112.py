
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
    # Create a CSV writer
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, DATA)
        writer.writeheader()
        for i in range(0, 24):
            # Generate random data for each hour
            data = {
                'Temperature': random.randint(RANGE['Temperature'][0], RANGE['Temperature'][1]),
                'Humidity': random.randint(RANGE['Humidity'][0], RANGE['Humidity'][1]),
                'Pressure': random.randint(RANGE['Pressure'][0], RANGE['Pressure'][1])
            }
            writer.writerow(data)
    return file_name