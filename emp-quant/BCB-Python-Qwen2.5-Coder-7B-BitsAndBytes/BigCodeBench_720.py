
import os
import csv
import random
from datetime import datetime

def task_func():
    # Define the file path
    file_path = 'task_func_data/Output.txt'
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Open the file in append mode
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers if the file is empty
        if file.tell() == 0:
            writer.writerow(['Timestamp', 'Temperature', 'Humidity'])
        
        # Generate random data and write to the file
        for _ in range(5):  # Example: Writing 5 rows of data
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            temperature = round(random.uniform(20, 30), 2)  # Random temperature between 20 and 30
            humidity = round(random.uniform(40, 60), 2)  # Random humidity between 40 and 60
            writer.writerow([timestamp, temperature, humidity])
    
    # Return the path to the CSV file
    return file_path

# Call the function and print the result
file_path = task_func()
print(f"The path to the CSV file is: {file_path}")