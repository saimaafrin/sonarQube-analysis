import os
import re
import pandas as pd
def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.
    This function walks through the directory, matches filenames against the pattern,
    and saves the matched file paths to a CSV file. It returns a DataFrame of these paths
    with a single column 'File Path'.

    :param pattern: Regex pattern to match filenames.
    :param directory: Directory to search for files.
    :param output_csv: Path to save the CSV file with matched file paths.
    :return: pd.DataFrame: DataFrame with a single column 'File Path' of matched paths.
    """
    matched_files = []
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file name matches the pattern
            if re.match(pattern, file):
                matched_files.append(os.path.join(root, file))
    
    # Create a DataFrame with the matched file paths
    df = pd.DataFrame(matched_files, columns=['File Path'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    
    return df