
import os
import pandas as pd
import re

def task_func(file_path: str) -> pd.DataFrame:
    # Define the regular expression pattern to match log entries
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}) - ([A-Z]+) - (.*)')
    
    # Initialize an empty list to store the extracted log entries
    log_entries = []
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Open the log file and read line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Match the line against the log pattern
            match = log_pattern.match(line)
            if match:
                # Extract the timestamp, level, and message from the matched line
                timestamp, level, message = match.groups()
                # Append the extracted data as a tuple to the log_entries list
                log_entries.append((timestamp, level, message))
    
    # Create a DataFrame from the log_entries list
    df = pd.DataFrame(log_entries, columns=['Timestamp', 'Level', 'Message'])
    
    return df