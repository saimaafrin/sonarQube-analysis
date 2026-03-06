
import csv
import os

def task_func(data, file_path, headers):
    if file_path is None:
        raise ValueError("'file_path' cannot be None")

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

    return os.path.abspath(file_path)

print(task_func(data, file_path, headers))