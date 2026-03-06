
import csv
import sys

def task_func(filename):
    # Read all lines from the CSV file
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        lines = list(reader)

    # Inverse the order of the lines
    lines.reverse()

    # Write the inverted lines back into the file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

    # Reset the cursor to the beginning of the file
    with open(filename, mode='r') as file:
        file.seek(0)

    return filename