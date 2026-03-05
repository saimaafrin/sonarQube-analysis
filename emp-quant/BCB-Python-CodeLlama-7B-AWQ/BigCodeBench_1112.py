import csv
import random
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}
def task_func(file_name="data.csv"):
    """
    Generate a CSV file with weather data for each hour of the current day.
    """
    # Create a new CSV file
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(DATA)
        # Write the data rows
        for i in range(24):
            row = []
            for data in DATA:
                row.append(random.randint(RANGE[data][0], RANGE[data][1]))
            writer.writerow(row)
    return file_name