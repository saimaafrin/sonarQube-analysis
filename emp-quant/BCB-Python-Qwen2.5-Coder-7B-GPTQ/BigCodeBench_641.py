import os
import re
import pandas as pd
def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    # Initialize an empty list to store matched file paths
    matched_paths = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file name matches the given regex pattern
            if re.match(pattern, file):
                # If it matches, append the full path to the list
                matched_paths.append(os.path.join(root, file))
    
    # Create a DataFrame from the list of matched paths
    df = pd.DataFrame(matched_paths, columns=['File Path'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    
    # Return the DataFrame
    return df