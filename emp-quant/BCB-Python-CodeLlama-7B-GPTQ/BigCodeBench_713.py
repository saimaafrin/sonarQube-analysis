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
    formatted_lines = []
    with open(log_file_path, 'r') as f:
        for line in f:
            for keyword in keywords:
                if keyword in line:
                    timestamp, message = line.split(' ', 1)
                    formatted_line = f'{keyword:20} {timestamp:20} {message}'
                    formatted_lines.append(formatted_line)
    return formatted_lines
log_file_path = 'example.log'
keywords = ['error', 'warning', 'info']