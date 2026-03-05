
import os
import pandas as pd
import re

def task_func(file_path: str) -> pd.DataFrame:
    """
    Parse a log file to extract log entries into a DataFrame.
    This function reads a log file line by line.
    The log file is assumed to follow this format for each entry:
    YYYY-MM-DD HH:MM:SS.ssssss - LEVEL - Message
    The function matches each line against a predefined regular expression to extract timestamp, log level, and message, ignoring lines where there is no match.
    It then aggregates the matched and extracted data into a pandas DataFrame with columns: 'Timestamp', 'Level', and 'Message'.
    If the logs are empty or there is no extracted data, this function returns an otherwise empty DataFrame containing the same expected columns.
    The function should raise the exception for:
    FileNotFoundError: If the specified log file does not exist.
    The function should output with:
    pd.DataFrame: A DataFrame with columns 'Timestamp', 'Level', and 'Message'.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file {file_path} does not exist.")

    df = pd.DataFrame(columns=['Timestamp', 'Level', 'Message'])

    with open(file_path, 'r') as f:
        for line in f:
            match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:{2}\d{2}.\d{6}) - (INFO|WARNING|ERROR) - (.*)", line)
            if match:
                df = df.append({
                    'Timestamp': match.group(1),
                    'Level': match.group(2),
                    'Message': match.group(3)
                }, ignore_index=True)

    return df