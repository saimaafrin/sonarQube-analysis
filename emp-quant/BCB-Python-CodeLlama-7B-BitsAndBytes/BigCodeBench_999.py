
import urllib.request
import os
import csv
import collections

def task_func(url, column_name, csv_file_path):
    # Download the CSV file from the given URL
    response = urllib.request.urlopen(url)
    csv_data = response.read().decode('utf-8')

    # Create a temporary file to store the downloaded CSV data
    temp_file = open(csv_file_path, 'wb')
    temp_file.write(csv_data.encode('utf-8'))
    temp_file.close()

    # Open the temporary file and read it as a CSV file
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)

        # Check if the specified column exists in the CSV file
        column_names = [row[0] for row in reader]
        if column_name not in column_names:
            os.remove(csv_file_path)
            raise ValueError(f"The provided column_name '{column_name}' does not exist in the CSV file.")

        # Create a dictionary to store the counts of each value in the specified column
        counts = collections.defaultdict(int)

        # Iterate over the rows in the CSV file and count the occurrences of each value in the specified column
        for row in reader:
            counts[row[column_names.index(column_name)]] += 1

    # Delete the temporary file
    os.remove(csv_file_path)

    # Return the dictionary of counts
    return counts

counts = task_func(url, column_name, csv_file_path)
print(counts)