
import re
import pandas as pd
from datetime import datetime

def task_func(log_file):
    # Define regular expression pattern to match log entries
    pattern = r"^(\w+): \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] - (.*)$"

    # Create list to store structured log data
    log_data = []

    # Open log file and read lines
    with open(log_file, "r") as f:
        for line in f:
            # Match log entry with regular expression pattern
            match = re.match(pattern, line)
            if match:
                # Extract message type, timestamp, and message from match
                message_type = match.group(1)
                timestamp = datetime.strptime(match.group(2), "%Y-%m-%d %H:%M:%S")
                message = match.group(3)

                # Add structured log data to list
                log_data.append((message_type, timestamp, message))

    # Create Pandas DataFrame from log data
    df = pd.DataFrame(log_data, columns=["Message Type", "Timestamp", "Message"])

    # Save DataFrame to CSV file
    csv_file = "structured_log.csv"
    df.to_csv(csv_file, index=False)

    # Return file path to CSV file
    return csv_file