
import re
import pandas as pd
from datetime import datetime

def task_func(log_file):
    # Define the regular expression pattern for the log entries
    pattern = r'TYPE: \[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\] - (.+)'
    
    # Initialize an empty list to store the log entries
    log_entries = []
    
    # Open the log file and read the contents
    with open(log_file, 'r') as f:
        for line in f:
            # Use the regular expression to match the log entries
            match = re.match(pattern, line)
            if match:
                # If the timestamp is valid, add the log entry to the list
                timestamp = match.group(1)
                message = match.group(2)
                log_entries.append((timestamp, message))
    
    # If no valid log entries were found, raise a ValueError
    if not log_entries:
        raise ValueError('No valid log entries found')
    
    # Convert the log entries to a pandas DataFrame
    df = pd.DataFrame(log_entries, columns=['timestamp', 'message'])
    
    # Define the file path for the new CSV file
    csv_file = 'structured_logs.csv'
    
    # Write the DataFrame to the CSV file
    df.to_csv(csv_file, index=False)
    
    # Return the file path to the newly created CSV file
    return csv_file