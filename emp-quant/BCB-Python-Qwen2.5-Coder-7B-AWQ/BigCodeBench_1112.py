import csv
import random
DATA = ['Temperature', 'Humidity', 'Pressure']
RANGE = {
    'Temperature': (-50, 50),
    'Humidity': (0, 100),
    'Pressure': (980, 1040)
}
def task_func(file_name="data.csv"):
    # Generate data for each hour of the current day
    data = {}
    for hour in range(24):
        data[hour] = {
            'Temperature': random.randint(RANGE['Temperature'][0], RANGE['Temperature'][1]),
            'Humidity': random.randint(RANGE['Humidity'][0], RANGE['Humidity'][1]),
            'Pressure': random.randint(RANGE['Pressure'][0], RANGE['Pressure'][1])
        }
    
    # Write data to CSV file
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['Hour'] + DATA)
        # Write data rows
        for hour, values in data.items():
            writer.writerow([hour] + [values[metric] for metric in DATA])
    
    return file_name