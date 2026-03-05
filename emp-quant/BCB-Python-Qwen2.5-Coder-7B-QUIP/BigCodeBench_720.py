
import os
import csv
import random
from datetime import datetime

def task_func():
    # Define the path to the output file
    output_file_path = "task_func_data/Output.txt"
    
    # Check if the directory exists, if not, create it
    output_dir = os.path.dirname(output_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Open the file in append mode
    with open(output_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write a header row
        writer.writerow(['Timestamp', 'Temperature', 'Humidity'])
        
        # Generate and write 10 random data rows
        for _ in range(10):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            temperature = random.randint(20, 40)  # Random temperature between 20 and 40
            humidity = random.randint(30, 60)  # Random humidity between 30 and 60
            writer.writerow([timestamp, temperature, humidity])
    
    # Return the path to the output file
    return output_file_path