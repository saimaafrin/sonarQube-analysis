
import os
import csv
import random
from datetime import datetime

def task_func():
    # Define the path to the CSV file
    file_path = "task_func_data/Output.txt"
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Open the CSV file in append mode
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header if the file is empty
        if os.path.getsize(file_path) == 0:
            writer.writerow(['Timestamp', 'Temperature', 'Humidity'])
        
        # Generate random sensor data
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        temperature = random.uniform(20.0, 30.0)
        humidity = random.uniform(40.0, 60.0)
        
        # Write the data to the CSV file
        writer.writerow([timestamp, temperature, humidity])
    
    # Return the path to the CSV file
    return file_path