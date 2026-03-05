import os
import csv
import random
from statistics import mean
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100
def task_func(filename):
    # Create a new CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(COLUMNS)

        # Generate simulated data for 100 people
        for i in range(PEOPLE_COUNT):
            name = f'Person {i}'
            age = random.randint(18, 65)
            height = random.randint(150, 200)
            weight = random.randint(50, 150)
            writer.writerow([name, age, height, weight])

    # Calculate and append the average age, height, and weight
    with open(filename, 'a', newline='') as csvfile:
        reader = csv.reader(csvfile)
        age_sum = 0
        height_sum = 0
        weight_sum = 0
        for row in reader:
            age_sum += int(row[1])
            height_sum += int(row[2])
            weight_sum += int(row[3])
        average_age = age_sum / PEOPLE_COUNT
        average_height = height_sum / PEOPLE_COUNT
        average_weight = weight_sum / PEOPLE_COUNT
        writer.writerow([f'Average age: {average_age}', f'Average height: {average_height}', f'Average weight: {average_weight}'])

    return filename