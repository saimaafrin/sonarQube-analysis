import csv
import sys
def task_func(filename):
    # Read all lines from the CSV file
    with open(filename, mode='r', newline='') as file:
        lines = file.readlines()
    
    # Invert the order of the lines
    lines = lines[::-1]
    
    # Write the inverted lines back into the file
    with open(filename, mode='w', newline='') as file:
        file.writelines(lines)
    
    # Reset the cursor to the beginning of the file
    with open(filename, mode='r', newline='') as file:
        file.seek(0)
    
    return filename