
import os
import re

def task_func(log_file_path: str, keywords: list):
    """
    Check a log file and format the lines that contain certain keywords.

    Args:
        log_file_path (str): Path to the log file.
        keywords (list): List of keywords to search for.

    Returns:
        formatted_lines (list): List of formatted strings containing the relevant information.
    """
    formatted_lines = []

    # Open the log file
    with open(log_file_path, 'r') as log_file:
        # Read the log file line by line
        for line in log_file:
            # Check if the line contains any of the keywords
            if any(keyword in line for keyword in keywords):
                # Extract the timestamp and message from the line
                timestamp, message = re.split(r'\s+', line.strip())

                # Format the line with 20 spaces between the keyword, timestamp, and message
                formatted_line = f'{keyword:20} {timestamp:20} {message}'

                # Add the formatted line to the list
                formatted_lines.append(formatted_line)

    return formatted_lines