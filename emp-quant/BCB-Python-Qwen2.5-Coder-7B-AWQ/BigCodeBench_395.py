import re
import os
import glob
import natsort
import pandas as pd
def task_func(directory='./', file_pattern='*.txt', regex=r'([0-9]+)'):
    """
    Extract numeric data from all text files matching a given pattern in a directory and compile it into a Pandas DataFrame.
    
    Parameters:
    - directory (str): The directory to search for text files. Defaults to the current directory.
    - file_pattern (str): The pattern to match text files. Defaults to '*.txt'.
    - regex (str): The regular expression to extract numeric data. Defaults to r'([0-9]+)'.
    
    Returns:
    - DataFrame: A pandas DataFrame with two columns: 'Filename' and 'Numeric Data'. Each row represents a file and its extracted numeric data.
    
    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    - ValueError: If no files matching the pattern are found.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Find all files matching the pattern
    file_paths = glob.glob(os.path.join(directory, file_pattern))
    if not file_paths:
        raise ValueError(f"No files matching the pattern {file_pattern} found in {directory}.")
    
    # Initialize a list to store the results
    results = []
    
    # Iterate over the files
    for file_path in natsort.natsorted(file_paths):
        with open(file_path, 'r') as file:
            content = file.read()
            # Find all matches of the regex
            matches = re.findall(regex, content)
            # Convert matches to integers
            numeric_data = [int(match) for match in matches]
            # Append the filename and numeric data to the results list
            results.append({'Filename': os.path.basename(file_path), 'Numeric Data': numeric_data})
    
    # Create a DataFrame from the results
    df = pd.DataFrame(results)
    
    return df