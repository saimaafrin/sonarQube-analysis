
import os
import re
import pandas as pd

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.
    
    Args:
    pattern (str): The regex pattern to match against filenames.
    directory (str): The directory to search for files.
    output_csv (str): The path to save the CSV file containing matched file paths.
    
    Returns:
    pd.DataFrame: DataFrame with a single column 'File Path' of matched paths.
    """
    matched_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file name matches the pattern
            if re.match(pattern, file):
                matched_files.append(os.path.join(root, file))
    
    # Create a DataFrame with the matched file paths
    df = pd.DataFrame(matched_files, columns=['File Path'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    
    return df