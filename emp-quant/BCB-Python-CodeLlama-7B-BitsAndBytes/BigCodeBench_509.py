
import pandas as pd
import csv
from difflib import ndiff

def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    # Read the files
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        reader1 = csv.reader(file1, delimiter=delimiter, quotechar=quotechar)
        reader2 = csv.reader(file2, delimiter=delimiter, quotechar=quotechar)

        # Create a list to store the differences
        differences = []

        # Iterate over the lines of the files
        for line1, line2 in zip(reader1, reader2):
            # If the lines are the same, continue
            if line1 == line2:
                continue

            # If the lines are different, add them to the differences list
            differences.append({
                'Line Number': reader1.line_num,
                'Status': ' ',
                'Content': line1
            })

            # If the line is only in file1, add it to the differences list
            if line1 not in line2:
                differences.append({
                    'Line Number': reader1.line_num,
                    'Status': '-',
                    'Content': line1
                })

            # If the line is only in file2, add it to the differences list
            if line2 not in line1:
                differences.append({
                    'Line Number': reader2.line_num,
                    'Status': '+',
                    'Content': line2
                })

    # Create a DataFrame from the differences list
    differences_df = pd.DataFrame(differences)

    # Return the DataFrame
    return differences_df