
import re
import pandas as pd
from datetime import datetime

def task_func(log_file):
    # Create a regular expression to extract the message type, timestamp, and message from the log file
    regex = r"TYPE: \[(?P<timestamp>.*)\] - (?P<message>.*)"
    with open(log_file, "r") as f:
        # Read the log file and extract the message type, timestamp, and message
        for line in f:
            match = re.search(regex, line)
            if match:
                timestamp = datetime.strptime(match.group("timestamp"), "%Y-%m-%d %H:%M:%S")
                message = match.group("message")
                yield (timestamp, message)
    # Create a Pandas DataFrame to store the structured log data
    df = pd.DataFrame(data=list(task_func(log_file)), columns=["timestamp", "message"])
    # Convert the DataFrame to a CSV file
    csv_file = "log_data.csv"
    df.to_csv(csv_file, index=False)
    return csv_file