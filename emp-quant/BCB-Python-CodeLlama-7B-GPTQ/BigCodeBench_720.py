import os
import csv
import random
from datetime import datetime
def task_func():
    # Create a CSV file "task_func_data/Output.txt"
    with open("task_func_data/Output.txt", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Temperature", "Humidity"])

    # Generate random data for temperature and humidity
    for i in range(10):
        temperature = random.uniform(20, 30)
        humidity = random.uniform(40, 60)
        csvwriter.writerow([temperature, humidity])

    # Delete the CSV file
    os.remove("task_func_data/Output.txt")

    # Return the path to the CSV file
    return "task_func_data/Output.txt"