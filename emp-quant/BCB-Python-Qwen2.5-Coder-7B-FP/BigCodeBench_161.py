import re
import pandas as pd
from datetime import datetime
def task_func(log_file):
    # Define the regular expression pattern for log entries
    pattern = r'(\w+): \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] - (.+)'
    
    # Initialize an empty list to store the log entries
    logs = []
    
    # Open the log file and read line by line
    with open(log_file, 'r') as file:
        for line in file:
            # Use the regular expression to match the log entry
            match = re.match(pattern, line)
            if match:
                # Extract the message type, timestamp, and message from the log entry
                message_type = match.group(1)
                timestamp = match.group(2)
                message = match.group(3)
                
                # Convert the timestamp to a datetime object
                try:
                    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    # Raise an exception if the timestamp is invalid
                    raise ValueError("Invalid timestamp in log entry")
                
                # Append the log entry to the list
                logs.append({'message_type': message_type, 'timestamp': timestamp, 'message': message})
    
    # Check if any valid log entries were found
    if not logs:
        # Raise an exception if no valid log entries were found
        raise ValueError("No valid log entries found")
    
    # Create a pandas DataFrame from the log entries
    df = pd.DataFrame(logs)
    
    # Define the file path for the new CSV file
    csv_file = 'structured_logs.csv'
    
    # Write the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    
    # Return the file path to the new CSV file
    return csv_file