import pandas as pd
import csv
from difflib import ndiff
def task_func(file_path1, file_path2, delimiter=',', quotechar='"'):
    """
    Compare two CSV files and create a difference report.

    Args:
        file_path1 (str): Path to the first CSV file.
        file_path2 (str): Path to the second CSV file.
        delimiter (str): Delimiter used in the CSV files.
        quotechar (str): Quote character used in the CSV files.

    Returns:
        DataFrame: A pandas DataFrame with the differences.

    Raises:
        FileNotFoundError: If either of the files cannot be found.
        ValueError: If either of the files is empty.
        Exception: For other IO related errors.
    """
    # Check if the files exist
    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
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
        for line1, line2 in zip(reader1, reader2):
            if line1 != line2:
                differences.append((line1, line2))

        # Create a DataFrame with the differences
        df = pd.DataFrame(differences, columns=['Line Number', 'Status', 'Content'])
        df['Line Number'] = df.index + 1
        df['Status'] = df['Line Number'].apply(lambda x: ' ' if x == 0 else '-' if x < 0 else '+')
        df['Content'] = df['Line Number'].apply(lambda x: line1 if x < 0 else line2)

        return df
file_path1 = 'file1.csv'
file_path2 = 'file2.csv'