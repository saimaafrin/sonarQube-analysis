import re
import pandas as pd
from datetime import datetime
def task_func(log_file):
    # Define the regular expression pattern for log entries
    pattern = r'(\w+): \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] - (.*)'
    
    # Initialize an empty list to store log data
    log_data = []
    
    # Open the log file and read line by line
    with open(log_file, 'r') as file:
        for line in file:
            # Use regular expression to match the log pattern
            match = re.match(pattern, line.strip())
            if match:
                # Extract the message type, timestamp, and message from the log entry
                message_type, timestamp, message = match.groups()
                
                # Convert the timestamp to a datetime object
                try:
                    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    # Raise an exception if the timestamp is invalid
                    raise ValueError("Invalid timestamp in log entry")
                
                # Append the log data to the list
                log_data.append([message_type, timestamp, message])
    
    # Check if any valid log entries were found
    if not log_data:
        # Raise an exception if no valid log entries are found
        raise ValueError("No valid log entries found")
    
    # Create a pandas DataFrame from the log data
    df = pd.DataFrame(log_data, columns=['Message Type', 'Timestamp', 'Message'])
    
    # Define the file path for the new CSV file
    csv_file = 'structured_logs.csv'
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)
    
    # Return the file path to the newly created CSV file
    return csv_file