import csv
import os
def task_func(data, file_path, headers):
    """
    Writes a list of tuples to a CSV file. Each tuple in the 'data' list represents a row in the CSV file, with each element of the tuple corresponding to a cell in the row. If a tuple contains fewer elements than there are headers, the missing elements are filled with None.
    """
    if file_path is None:
        raise ValueError("file_path cannot be None")

    # Create the CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the headers
        writer.writerow(headers)

        # Write the data
        for row in data:
            writer.writerow(row)

    # Return the absolute path of the saved CSV file
    return os.path.abspath(file_path)
data = [
    ('test', 123, 2),
    (3, -3, -15),
    ('hallo', 1, -2),
    ('1', 'hi', 'hello')
]
file_path = 'data.csv'
headers = ['test1', 'test2', 'test3']