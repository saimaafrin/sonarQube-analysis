import os
import pandas as pd
import re
def task_func(file_path: str) -> pd.DataFrame:
    # Define the regular expression pattern for log entries
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{6}) - ([A-Z]+) - (.*)')

    # Initialize an empty list to store the log entries
    log_entries = []

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified log file does not exist: {file_path}")

    # Read the log file line by line
    with open(file_path, 'r') as file:
        for line in file:
            # Match the line against the regular expression
            match = log_pattern.match(line)
            if match:
                # Extract timestamp, log level, and message
                timestamp, level, message = match.groups()
                # Append the extracted data to the list
                log_entries.append({'Timestamp': timestamp, 'Level': level, 'Message': message})

    # Create a DataFrame from the list of log entries
    df = pd.DataFrame(log_entries)

    return df