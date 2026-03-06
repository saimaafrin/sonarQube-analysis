
import os
import csv
import random
from datetime import datetime

def task_func():
    # Create a CSV file with random temperature and humidity data
    file_path = "task_func_data/Output.txt"
    with open(file_path, "a") as csv_file:
        writer = csv.writer(csv_file)
        for i in range(10):
            writer.writerow([random.randint(10, 30), random.randint(30, 70)])

    # Delete the CSV file
    os.remove(file_path)

    # Return the path to the CSV file
    return file_path

# Call the function and print the output
print(task_func())