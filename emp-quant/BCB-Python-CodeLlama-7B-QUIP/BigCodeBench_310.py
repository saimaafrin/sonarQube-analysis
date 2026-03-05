
import os
import csv
import random
from statistics import mean
# Constants
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100
def task_func(filename):
    # Create the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, COLUMNS)
        writer.writeheader()
        for i in range(PEOPLE_COUNT):
            person = {
                'Name': f'Person {i+1}',
                'Age': random.randint(18, 100),
                'Height': random.randint(100, 250),
                'Weight': random.randint(50, 200)
            }
            writer.writerow(person)
    # Calculate the average age, height, and weight
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        age_sum = 0
        height_sum = 0
        weight_sum = 0
        for row in reader:
            age_sum += row['Age']
            height_sum += row['Height']
            weight_sum += row['Weight']
        average_age = age_sum / PEOPLE_COUNT
        average_height = height_sum / PEOPLE_COUNT
        average_weight = weight_sum / PEOPLE_COUNT
    # Print the results
    print(f'Average age: {average_age}')
    print(f'Average height: {average_height}')
    print(f'Average weight: {average_weight}')
    return filename