
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

    # Open the log file and read its contents
    with open(log_file_path, 'r') as f:
        contents = f.read()

    # Search for lines containing any of the keywords
    for keyword in keywords:
        pattern = re.compile(r'(?<!\d)\b' + keyword + r'\b(?!\d)')
        matches = pattern.findall(contents)

        # Format each match and add it to the list
        for match in matches:
            timestamp, message = match.split(' ', 1)
            formatted_line = f'{keyword:20} {timestamp:20} {message}'
            formatted_lines.append(formatted_line)

    return formatted_lines

# Print the formatted lines
for formatted_line in formatted_lines:
    print(formatted_line)