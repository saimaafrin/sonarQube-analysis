
import re
import pandas as pd
from datetime import datetime

def task_func(log_file):
    # Define the regular expression pattern for extracting log entries
    pattern = r'(\w+): \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] - (.+)'
    
    # Initialize an empty list to store the extracted log entries
    logs = []
    
    # Open the log file and read line by line
    with open(log_file, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                log_type, timestamp, message = match.groups()
                try:
                    # Convert the timestamp string to a datetime object
                    dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    logs.append({'Type': log_type, 'Timestamp': dt, 'Message': message})
                except ValueError:
                    # Raise an exception if the timestamp is invalid
                    raise ValueError("Invalid timestamp in log entry.")
    
    # Check if any valid log entries were found
    if not logs:
        raise ValueError("No valid log entries found.")
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(logs)
    
    # Define the output CSV file path
    csv_file = 'structured_logs.csv'
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    
    # Return the file path to the newly created CSV file
    return csv_file