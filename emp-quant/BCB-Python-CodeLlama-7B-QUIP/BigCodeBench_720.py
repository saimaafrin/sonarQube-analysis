
import os
import csv
import random
from datetime import datetime

def task_func():
    # Create the CSV file
    file_path = "task_func_data/Output.txt"
    with open(file_path, "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Temperature", "Humidity"])

    # Generate random data
    for i in range(10):
        temperature = random.uniform(20, 30)
        humidity = random.uniform(40, 60)
        csv_writer.writerow([temperature, humidity])

    # Delete the file
    os.remove(file_path)

    return file_path