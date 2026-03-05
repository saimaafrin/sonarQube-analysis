import urllib.request
import os
import csv
import collections
def task_func(url, column_name, csv_file_path):
    """
    Download a CSV file from a given URL, save it to a specified path, and count the occurrences of each value in a particular column.
    The function handles various scenarios including missing columns and file download errors.
    """
    # Download the CSV file
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            with open(csv_file_path, 'wb') as f:
                f.write(data)
    except urllib.error.URLError as e:
        print(f"Error downloading file from {url}: {e}")
        return None

    # Count the occurrences of each value in the specified column
    try:
        with open(csv_file_path, 'r') as f:
            reader = csv.reader(f)
            column_index = next(reader).index(column_name)
            counts = collections.Counter()
            for row in reader:
                counts[row[column_index]] += 1
            return counts
    except csv.Error as e:
        print(f"Error reading CSV file {csv_file_path}: {e}")
        return None
    finally:
        os.remove(csv_file_path)
url = "https://example.com/data.csv"
column_name = "column_name"
csv_file_path = "data.csv"