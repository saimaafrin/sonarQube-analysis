import os
import re
def task_func(log_file_path: str, keywords: list):
    """
    Check a log file and format the lines that contain certain keywords.

    Args:
        log_file_path (str): Path to the log file.
        keywords (list): List of keywords to search for in the log file.

    Returns:
        formatted_lines (list): List of formatted strings containing the relevant information.
    """
    # Read the log file
    with open(log_file_path, 'r') as f:
        lines = f.readlines()

    # Create a list to store the formatted lines
    formatted_lines = []

    # Loop through each line in the log file
    for line in lines:
        # Check if the line contains any of the keywords
        for keyword in keywords:
            if keyword in line:
                # Extract the timestamp and message from the line
                timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line).group()
                message = re.search(r'(?<=message=).*', line).group()

                # Format the line with 20 spaces between the keyword, timestamp, and message
                formatted_line = f"{keyword:20} {timestamp:20} {message}"

                # Add the formatted line to the list
                formatted_lines.append(formatted_line)

    return formatted_lines
log_file_path = 'example.log'
keywords = ['error', 'warning']