import os
import csv
import random
from datetime import datetime
def task_func():
    # Create a CSV file with random data
    with open('task_func_data/Output.txt', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Temperature', 'Humidity'])
        for i in range(10):
            writer.writerow([random.randint(0, 100), random.randint(0, 100)])

    # Delete the CSV file
    os.remove('task_func_data/Output.txt')

    # Return the path to the CSV file
    return 'task_func_data/Output.txt'