
import os
import pandas as pd
import re

def task_func(file_path: str) -> pd.DataFrame:
    """
    Parse a log file to extract log entries into a DataFrame.

    Args:
        file_path (str): Path to the log file.

    Returns:
        pd.DataFrame: A DataFrame with columns 'Timestamp', 'Level', and 'Message'.

    Raises:
        FileNotFoundError: If the specified log file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file {file_path} does not exist.")

    # Define regular expression to match log entries
    log_entry_regex = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}) - (\w+) - (.*)"

    # Initialize DataFrame with expected columns
    df = pd.DataFrame(columns=["Timestamp", "Level", "Message"])

    # Open log file and read line by line
    with open(file_path, "r") as f:
        for line in f:
            # Match log entry against regular expression
            match = re.match(log_entry_regex, line)
            if match:
                # Extract timestamp, level, and message
                timestamp = match.group(1)
                level = match.group(2)
                message = match.group(3)

                # Append extracted data to DataFrame
                df = df.append({"Timestamp": timestamp, "Level": level, "Message": message}, ignore_index=True)

    # Return DataFrame with log entries
    return df