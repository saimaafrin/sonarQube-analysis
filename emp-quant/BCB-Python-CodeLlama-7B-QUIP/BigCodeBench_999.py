
import urllib.request
import os
import csv
import collections

def task_func(url, column_name, csv_file_path):
    try:
        # Download the CSV file
        response = urllib.request.urlopen(url)
        # Save the file to the specified path
        with open(csv_file_path, 'wb') as f:
            f.write(response.read())
    except urllib.error.HTTPError:
        # Handle HTTP errors
        raise ValueError("The provided URL is not valid")
    except FileNotFoundError:
        # Handle file not found errors
        raise ValueError("The specified file path does not exist")
    try:
        # Open the CSV file
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            # Get the specified column
            column = next(reader)
            # Get the values in the specified column
            values = [row[column_name] for row in reader]
            # Count the occurrences of each value
            counts = collections.Counter(values)
            # Return the dictionary of counts
            return {value: counts[value] for value in counts}
    except csv.Error:
        # Handle CSV errors
        raise ValueError("The CSV file is not valid")
    finally:
        # Delete the downloaded file
        os.remove(csv_file_path)