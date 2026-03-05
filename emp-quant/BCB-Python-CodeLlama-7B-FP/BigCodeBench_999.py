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
    except urllib.error.URLError as e:
        print(f"Error downloading file from {url}: {e}")
        return None

    # Save the CSV file to the specified path
    try:
        with open(csv_file_path, "wb") as f:
            f.write(data)
    except OSError as e:
        print(f"Error saving file to {csv_file_path}: {e}")
        return None

    # Count the occurrences of each value in the specified column
    try:
        with open(csv_file_path, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            column_index = header.index(column_name)
            counts = collections.Counter()
            for row in reader:
                counts[row[column_index]] += 1
    except csv.Error as e:
        print(f"Error reading file {csv_file_path}: {e}")
        return None

    # Delete the downloaded CSV file
    try:
        os.remove(csv_file_path)
    except OSError as e:
        print(f"Error deleting file {csv_file_path}: {e}")
        return None

    return counts
url = "https://example.com/data.csv"
column_name = "column1"
csv_file_path = "data.csv"