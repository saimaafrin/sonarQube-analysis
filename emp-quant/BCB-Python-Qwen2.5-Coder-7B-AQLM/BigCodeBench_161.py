
import re
import pandas as pd
from datetime import datetime

def task_func(log_file):
    # Define the regular expression pattern to extract log entries
    pattern = r'(\w+): \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] - (.+)'
    
    # Initialize an empty list to store the log entries
    logs = []
    
    # Open the log file and read line by line
    with open(log_file, 'r') as file:
        for line in file:
            # Search for the pattern in each line
            match = re.match(pattern, line.strip())
            if match:
                # Extract the message type, timestamp, and message
                message_type, timestamp, message = match.groups()
                try:
                    # Validate the timestamp
                    datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    # Append the log entry to the list
                    logs.append({'Type': message_type, 'Timestamp': timestamp, 'Message': message})
                except ValueError:
                    # Raise an exception if the timestamp is invalid
                    raise ValueError("Invalid timestamp in log entry")
    
    # Check if any valid log entries were found
    if not logs:
        raise ValueError("No valid log entries found")
    
    # Create a DataFrame from the log entries
    df = pd.DataFrame(logs)
    
    # Define the output CSV file path
    output_csv = 'structured_logs.csv'
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    
    # Return the file path to the newly created CSV file
    return output_csv