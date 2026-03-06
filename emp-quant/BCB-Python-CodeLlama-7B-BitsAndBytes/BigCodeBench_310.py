
import os
import csv
import random
from statistics import mean

# Constants
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
                'Name': f'Person {i+1}',
                'Age': random.randint(18, 65),
                'Height': random.randint(150, 200),
                'Weight': random.randint(50, 150)
            })

    # Calculate and append the average age, height, and weight
    with open(filename, 'a', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        age_avg = mean(float(row['Age']) for row in reader)
        height_avg = mean(float(row['Height']) for row in reader)
        weight_avg = mean(float(row['Weight']) for row in reader)
        writer = csv.DictWriter(csvfile, fieldnames=['Average Age', 'Average Height', 'Average Weight'])
        writer.writerow({
            'Average Age': age_avg,
            'Average Height': height_avg,
            'Average Weight': weight_avg
        })

    return filename

# Call the function and get the path of the created CSV file
filename = task_func('simulated_data.csv')
print(f'CSV file created at: {filename}')