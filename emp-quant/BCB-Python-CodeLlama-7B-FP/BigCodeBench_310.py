import os
import csv
import random
from statistics import mean
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100
def task_func(filename):
    # Create a new CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
        writer.writeheader()

        # Generate simulated data for 100 people
        for i in range(PEOPLE_COUNT):
            writer.writerow({
                'Name': f'Person {i}',
                'Age': random.randint(18, 65),
                'Height': random.randint(150, 200),
                'Weight': random.randint(50, 150)
            })

        # Calculate and append the average age, height, and weight
        average_age = mean(row['Age'] for row in csv.DictReader(open(filename)))
        average_height = mean(row['Height'] for row in csv.DictReader(open(filename)))
        average_weight = mean(row['Weight'] for row in csv.DictReader(open(filename)))
        writer.writerow({
            'Average Age': average_age,
            'Average Height': average_height,
            'Average Weight': average_weight
        })

    return filename