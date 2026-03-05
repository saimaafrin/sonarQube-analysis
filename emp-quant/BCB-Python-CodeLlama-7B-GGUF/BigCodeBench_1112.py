
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
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(DATA)

        # Generate random data for each hour of the day
        for hour in range(24):
            # Generate random data for each data point
            data = [random.randint(*RANGE[data_point]) for data_point in DATA]
            # Write the data row
            writer.writerow(data)

    return file_name

# Call the function and get the path to the created file
file_path = task_func()
print(file_path)