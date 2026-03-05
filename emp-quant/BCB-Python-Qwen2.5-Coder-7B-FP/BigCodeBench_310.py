import os
import csv
import random
from statistics import mean
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100
def task_func(filename):
    # Generate random data for 100 people
    data = []
    for _ in range(PEOPLE_COUNT):
        name = f"Person{random.randint(1, 1000)}"
        age = random.randint(18, 65)
        height = random.uniform(140, 200)
        weight = random.uniform(40, 120)
        data.append([name, age, height, weight])

    # Calculate average values
    avg_age = mean([person[1] for person in data])
    avg_height = mean([person[2] for person in data])
    avg_weight = mean([person[3] for person in data])

    # Append average values to data
    data.append(['Average', avg_age, avg_height, avg_weight])

    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        writer.writerows(data)

    # Return the path of the created CSV file
    return os.path.abspath(filename)