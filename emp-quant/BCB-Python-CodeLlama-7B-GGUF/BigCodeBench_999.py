
import urllib.request
import os
import csv
import collections

def task_func(url, column_name, csv_file_path):
    """
    Download a CSV file from a given URL, save it to a specified path, and count the occurrences of each value in a particular column.

    Args:
        url (str): The URL of the CSV file to download.
        column_name (str): The name of the column to count values from.
        csv_file_path (str): The path to save the downloaded CSV file.

    Returns:
        dict: A dictionary mapping the values from the specified column to their
        corresponding occurrence counts.

    Raises:
        ValueError: If the specified column_name does not exist in the CSV file.
    """
    # Download the CSV file
    response = urllib.request.urlopen(url)
    csv_file = response.read()

    # Save the CSV file to the specified path
    with open(csv_file_path, 'wb') as f:
        f.write(csv_file)

    # Count the occurrences of each value in the specified column
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        column_index = None
        for row in reader:
            if column_name in row:
                column_index = row.index(column_name)
                break
        if column_index is None:
            raise ValueError(f"The provided column_name '{column_name}' does not exist in the CSV file.")
        counts = collections.Counter(row[column_index] for row in reader)

    # Delete the downloaded CSV file
    os.remove(csv_file_path)

    return counts