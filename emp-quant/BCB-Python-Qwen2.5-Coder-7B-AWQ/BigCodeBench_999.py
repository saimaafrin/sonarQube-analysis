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
        
        # Open the CSV file and read the data
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            
            # Check if the specified column exists
            if column_name not in reader.fieldnames:
                os.remove(csv_file_path)  # Delete the downloaded file
                raise ValueError(f"The provided column_name '{column_name}' does not exist in the CSV file.")
            
            # Count occurrences of each value in the specified column
            for row in reader:
                value_counts[row[column_name]] += 1
        
        # Delete the downloaded file
        os.remove(csv_file_path)
        
        return dict(value_counts)
    
    except urllib.error.URLError as e:
        # Handle file download errors
        print(f"Error downloading the file: {e}")
        return None