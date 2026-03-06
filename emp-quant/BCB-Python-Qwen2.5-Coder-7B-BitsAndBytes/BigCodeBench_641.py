
import os
import re
import pandas as pd

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.
    
    Args:
        pattern (str): The regex pattern to match against filenames.
        directory (str): The directory to search within.
        output_csv (str): The path to save the CSV file containing the matched file paths.
        
    Returns:
        pd.DataFrame: A DataFrame with a single column 'File Path' of matched paths.
    """
    # Initialize an empty list to store the matched file paths
    matched_paths = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the filename matches the pattern
            if re.match(pattern, file):
                # If it matches, add the full path to the list
                matched_paths.append(os.path.join(root, file))
    
    # Create a DataFrame from the list of matched paths
    df = pd.DataFrame(matched_paths, columns=['File Path'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    
    return df