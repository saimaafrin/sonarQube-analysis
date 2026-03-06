
import os
import csv
import random
from statistics import mean

# Constants
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100

def task_func(filename):
    # Generate random names
    names = [f"Person{i+1}" for i in range(PEOPLE_COUNT)]
    
    # Generate random ages between 20 and 60
    ages = [random.randint(20, 60) for _ in range(PEOPLE_COUNT)]
    
    # Generate random heights between 150 and 200 cm
    heights = [random.randint(150, 200) for _ in range(PEOPLE_COUNT)]
    
    # Generate random weights between 40 and 100 kg
    weights = [random.randint(40, 100) for _ in range(PEOPLE_COUNT)]
    
    # Create a list of dictionaries to store the data
    data = [{'Name': name, 'Age': age, 'Height': height, 'Weight': weight} 
            for name, age, height, weight in zip(names, ages, heights, weights)]
    
    # Calculate averages
    avg_age = mean(ages)
    avg_height = mean(heights)
    avg_weight = mean(weights)
    
    # Append averages as a new row
    data.append({'Name': 'Average', 'Age': avg_age, 'Height': avg_height, 'Weight': avg_weight})
    
    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(data)
    
    return filename