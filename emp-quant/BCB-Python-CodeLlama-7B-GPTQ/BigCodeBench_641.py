import os
import re
import pandas as pd
def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.
    This function walks through the directory, matches filenames against the pattern, and saves the matched file paths to a CSV file.
    It returns a DataFrame of these paths with colomn 'File Path'.
    """
    # Create a list to store the matched file paths
    matched_files = []

    # Walk through the directory and match filenames against the pattern
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                matched_files.append(os.path.join(root, file))

    # Save the matched file paths to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Path'])
        for file in matched_files:
            writer.writerow([file])

    # Return a DataFrame of the matched file paths
    return pd.DataFrame(matched_files, columns=['File Path'])
pattern = r'^[a-zA-Z0-9_-]+$'
directory = '.'
output_csv = 'matched_files.csv'