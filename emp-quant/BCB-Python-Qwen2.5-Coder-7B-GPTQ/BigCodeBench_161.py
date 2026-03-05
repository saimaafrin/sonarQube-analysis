import re
import pandas as pd
from datetime import datetime
def task_func(log_file):
    # Define the regular expression pattern for the log entries
    pattern = r'(\w+): \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] - (.*)'
    
    # Initialize an empty list to store the log entries
    logs = []
    
    # Open the log file and read line by line
    with open(log_file, 'r') as file:
        for line in file:
            # Match the log entry against the pattern
            match = re.match(pattern, line)
            if match:
                # Extract the log type, timestamp, and message
                log_type = match.group(1)
                timestamp = match.group(2)
                message = match.group(3)
                
                # Convert the timestamp to a datetime object
                try:
                    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    raise ValueError("Invalid timestamp in log entry")
                
                # Append the log entry to the list
                logs.append({'Type': log_type, 'Timestamp': timestamp, 'Message': message})
    
    # Check if any valid log entries were found
    if not logs:
        raise ValueError("No valid log entries found")
    
    # Create a DataFrame from the log entries
    df = pd.DataFrame(logs)
    
    # Define the output file path
    output_file = 'structured_logs.csv'
    
    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    
    # Return the file path to the newly created CSV file
    return output_file