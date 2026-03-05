import pandas as pd
import csv
from difflib import ndiff
def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    """
    Compare two CSV files and create a difference report.

    Args:
        file_path1 (str): Path to the first CSV file.
        file_path2 (str): Path to the second CSV file.
        delimiter (str, optional): Delimiter used in the CSV files. Defaults to ','.
        quotechar (str, optional): Quote character used in the CSV files. Defaults to '"'.

    Returns:
        DataFrame: A pandas DataFrame with the differences. The DataFrame contains the following columns:
            'Line Number': The line number in the file where the difference occurs.
            'Status': A character indicating the type of difference:
                ' ': No change (line is the same in both files).
                '-': Line present in the first file but not in the second.
                '+': Line present in the second file but not in the first.
            'Content': The actual text content of the line from either file.

    Raises:
        FileNotFoundError: If either of the files cannot be found.
        ValueError: If either of the files is empty.
        Exception: For other IO related errors.
    """
    # Check if the files exist
    if not (os.path.exists(file_path1) and os.path.exists(file_path2)):
        raise FileNotFoundError(f"File not found: {file_path1} or {file_path2}")

    # Check if the files are empty
    if os.path.getsize(file_path1) == 0 or os.path.getsize(file_path2) == 0:
        raise ValueError(f"File is empty: {file_path1} or {file_path2}")

    # Read the files
    with open(file_path1, 'r', newline='') as file1, open(file_path2, 'r', newline='') as file2:
        reader1 = csv.reader(file1, delimiter=delimiter, quotechar=quotechar)
        reader2 = csv.reader(file2, delimiter=delimiter, quotechar=quotechar)

        # Create a list of differences
        differences = []

        # Iterate over the lines in the files
        for line1, line2 in zip(reader1, reader2):
            # Check if the lines are the same
            if line1 == line2:
                # Add a space to the list of differences
                differences.append(' ')
            else:
                # Add a minus or plus sign to the list of differences
                differences.append('-' if line1 in line2 else '+')

        # Create a DataFrame with the differences
        df = pd.DataFrame(differences, columns=['Status', 'Content'])

        # Add the line numbers to the DataFrame
        df['Line Number'] = range(1, len(differences) + 1)

        # Return the DataFrame
        return df
file_path1 = 'file1.csv'
file_path2 = 'file2.csv'