import urllib.request
import os
import csv
import collections
def task_func(url, column_name, csv_file_path):
    try:
        # Download the CSV file
        urllib.request.urlretrieve(url, csv_file_path)
        
        # Initialize a dictionary to count occurrences
        value_counts = collections.defaultdict(int)
        
        # Open the CSV file and read data
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            
            # Check if the column_name exists in the CSV file
            if column_name not in reader.fieldnames:
                os.remove(csv_file_path)  # Delete the downloaded file
                raise ValueError(f"The provided column_name '{column_name}' does not exist in the CSV file.")
            
            # Count occurrences of each value in the specified column
            for row in reader:
                value_counts[row[column_name]] += 1
        
        # Delete the downloaded file after processing
        os.remove(csv_file_path)
        
        return dict(value_counts)
    
    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {e}")
        return None