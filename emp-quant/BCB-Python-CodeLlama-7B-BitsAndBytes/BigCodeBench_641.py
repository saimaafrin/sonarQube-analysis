
import os
import re
import pandas as pd

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.
    This function walks through the directory, matches filenames against the pattern, and saves the matched file paths to a CSV file.
    It returns a DataFrame of these paths with colomn 'File Path'.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(pattern, file):
                file_paths.append(os.path.join(root, file))
    df = pd.DataFrame({'File Path': file_paths})
    df.to_csv(output_csv, index=False)
    return df