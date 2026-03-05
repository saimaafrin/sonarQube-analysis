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
    # Check if the log file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Log file '{file_path}' does not exist.")

    # Define the regular expression to match each line
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}) - (\w+) - (.+)$"

    # Initialize an empty list to store the extracted data
    data = []

    # Open the log file and read line by line
    with open(file_path, "r") as f:
        for line in f:
            # Match the line against the regular expression
            match = re.match(pattern, line)

            # If there is a match, extract the timestamp, level, and message
            if match:
                timestamp, level, message = match.groups()
                data.append({"Timestamp": timestamp, "Level": level, "Message": message})

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data)

    # Return the DataFrame
    return df
file_path = "example.log"