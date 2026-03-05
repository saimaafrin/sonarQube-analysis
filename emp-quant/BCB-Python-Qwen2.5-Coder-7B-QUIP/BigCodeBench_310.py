
import os
import csv
import random
from statistics import mean
# Constants
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100

def task_func(filename):
    # Generate random data for 100 people
    data = []
    for _ in range(PEOPLE_COUNT):
        name = f"Person{random.randint(1, 1000)}"
        age = random.randint(18, 80)
        height = random.randint(140, 200)
        weight = random.randint(40, 150)
        data.append([name, age, height, weight])

    # Calculate averages
    average_age = mean(row[1] for row in data)
    average_height = mean(row[2] for row in data)
    average_weight = mean(row[3] for row in data)

    # Write data to CSV
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(COLUMNS)
        writer.writerows(data)
        writer.writerow(['Average', average_age, average_height, average_weight])

    return filename