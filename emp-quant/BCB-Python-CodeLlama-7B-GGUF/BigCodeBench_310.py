
import os
import csv
import random
from statistics import mean

# Constants
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100

def task_func(filename):
    # Create a CSV file with the given filename
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
        writer.writeheader()

        # Generate data for 100 people
        for i in range(PEOPLE_COUNT):
            # Generate random values for name, age, height, and weight
            name = f'Person {i+1}'
            age = random.randint(18, 65)
            height = random.randint(150, 200)
            weight = random.randint(50, 150)

            # Write the data to the CSV file
            writer.writerow({'Name': name, 'Age': age, 'Height': height, 'Weight': weight})

    # Calculate and append the average age, height, and weight
    with open(filename, 'a', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        age_avg = mean(float(row['Age']) for row in reader)
        height_avg = mean(float(row['Height']) for row in reader)
        weight_avg = mean(float(row['Weight']) for row in reader)
        writer = csv.DictWriter(csvfile, fieldnames=['Average Age', 'Average Height', 'Average Weight'])
        writer.writerow({'Average Age': age_avg, 'Average Height': height_avg, 'Average Weight': weight_avg})

    # Return the path of the created CSV file
    return filename