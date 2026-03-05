import os
import csv
import random
from datetime import datetime
def task_func():
    # Create a CSV file
    csv_file = "task_func_data/Output.txt"
    with open(csv_file, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Temperature', 'Humidity'])
        for i in range(10):
            writer.writerow([random.randint(10, 30), random.randint(10, 50)])
    return csv_file