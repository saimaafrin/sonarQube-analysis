
import re
import pandas as pd
from datetime import datetime

def task_func(log_file):
    # Read the log file and extract the log entries
    with open(log_file, 'r') as f:
        log_entries = f.read().splitlines()

    # Create a list to store the structured log data
    structured_data = []

    # Iterate over the log entries and extract the message type, timestamp, and message
    for log_entry in log_entries:
        # Extract the message type and timestamp from the log entry
        match = re.search(r'^(\w+):\s+(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}) - (.*)$', log_entry)
        if match:
            message_type = match.group(1)
            timestamp = datetime.strptime(match.group(2), '%Y-%m-%d %H:%M:%S')
            message = match.group(3)

            # Add the structured data to the list
            structured_data.append((message_type, timestamp, message))

    # Create a Pandas DataFrame from the structured data
    df = pd.DataFrame(structured_data, columns=['Message Type', 'Timestamp', 'Message'])

    # Write the DataFrame to a CSV file
    csv_file = 'structured_log.csv'
    df.to_csv(csv_file, index=False)

    return csv_file