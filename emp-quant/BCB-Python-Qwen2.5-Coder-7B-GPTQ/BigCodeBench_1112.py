import csv
import random
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}
def task_func(file_name="data.csv"):
    # Open the file in write mode
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(DATA)
        # Generate and write data for each hour of the day
        for _ in range(24):
            row = [random.randint(RANGE[col][0], RANGE[col][1]) for col in DATA]
            writer.writerow(row)
    # Return the path to the created file
    return file_name