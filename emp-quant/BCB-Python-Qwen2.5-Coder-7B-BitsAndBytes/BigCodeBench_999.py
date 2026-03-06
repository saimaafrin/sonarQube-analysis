
import urllib.request
import os
import csv
import collections

def task_func(url, column_name, csv_file_path):
    try:
        # Download the CSV file
        response = urllib.request.urlopen(url)
        temp_csv_path = 'temp.csv'
        with open(temp_csv_path, 'wb') as out_file:
            out_file.write(response.read())
        
        # Check if the column exists
        with open(temp_csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            if column_name not in headers:
                os.remove(temp_csv_path)
                raise ValueError(f"The provided column_name '{column_name}' does not exist in the CSV file.")
        
        # Count occurrences of each value in the specified column
        value_counts = collections.Counter()
        with open(temp_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                value_counts[row[column_name]] += 1
        
        # Delete the temporary CSV file
        os.remove(temp_csv_path)
        
        return dict(value_counts)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None