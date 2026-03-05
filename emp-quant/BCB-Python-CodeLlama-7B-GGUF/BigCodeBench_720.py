
import os
import csv
import random
from datetime import datetime

def task_func():
    # Create a CSV file with random temperature and humidity data
    with open('task_func_data/Output.txt', 'a', newline='') as csvfile:
        fieldnames = ['Temperature', 'Humidity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(10):
            temperature = random.uniform(20, 30)
            humidity = random.uniform(40, 60)
            writer.writerow({'Temperature': temperature, 'Humidity': humidity})

    # Delete the CSV file
    os.remove('task_func_data/Output.txt')

    # Return the path to the CSV file
    return 'task_func_data/Output.txt'