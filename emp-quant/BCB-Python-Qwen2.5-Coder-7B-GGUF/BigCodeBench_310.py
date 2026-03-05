
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
        name = f"Person{_ + 1}"
        age = random.randint(20, 60)
        height = random.randint(150, 200)
        weight = random.randint(50, 150)
        data.append([name, age, height, weight])

    # Calculate average values
    avg_age = mean([row[1] for row in data])
    avg_height = mean([row[2] for row in data])
    avg_weight = mean([row[3] for row in data])

    # Append average values to the data
    data.append(['Average', avg_age, avg_height, avg_weight])

    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        writer.writerows(data)

    # Return the path of the created CSV file
    return os.path.abspath(filename)