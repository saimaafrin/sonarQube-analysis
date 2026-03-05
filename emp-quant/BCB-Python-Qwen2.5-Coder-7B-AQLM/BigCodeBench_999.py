
import urllib.request
import os
import csv
import collections

def task_func(url, column_name, csv_file_path):
    try:
        # Download the CSV file
        urllib.request.urlretrieve(url, csv_file_path)
        
        # Initialize a counter for the column values
        value_counter = collections.Counter()
        
        # Read the CSV file and count occurrences of the specified column
        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if column_name in row:
                    value_counter[row[column_name]] += 1
                else:
                    raise ValueError(f"The provided column_name '{column_name}' does not exist in the CSV file.")
        
        # Delete the downloaded CSV file
        os.remove(csv_file_path)
        
        # Return the dictionary of value counts
        return dict(value_counter)
    
    except urllib.error.URLError as e:
        # Handle file download errors
        print(f"Error downloading the file: {e}")
        return None
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        return None