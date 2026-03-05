import os
import csv
import random
from statistics import mean
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100
def task_func(filename):
    # Create a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
        writer.writeheader()

        # Generate simulated data
        for i in range(PEOPLE_COUNT):
            writer.writerow({
                'Name': f'Person {i}',
                'Age': random.randint(18, 65),
                'Height': random.randint(150, 200),
                'Weight': random.randint(50, 150)
            })

    # Calculate and append the average age, height, and weight
    with open(filename, 'a', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        age_mean = mean(float(row['Age']) for row in reader)
        height_mean = mean(float(row['Height']) for row in reader)
        weight_mean = mean(float(row['Weight']) for row in reader)
        writer = csv.DictWriter(csvfile, fieldnames=['Average Age', 'Average Height', 'Average Weight'])
        writer.writerow({
            'Average Age': age_mean,
            'Average Height': height_mean,
            'Average Weight': weight_mean
        })

    return filename