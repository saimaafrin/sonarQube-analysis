import csv
import random
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}
def task_func(file_name="data.csv"):
    # Create a new CSV file
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(DATA)
        # Write the data rows
        for i in range(24):
            row = [random.randint(RANGE[data][0], RANGE[data][1]) for data in DATA]
            writer.writerow(row)
    return file_name