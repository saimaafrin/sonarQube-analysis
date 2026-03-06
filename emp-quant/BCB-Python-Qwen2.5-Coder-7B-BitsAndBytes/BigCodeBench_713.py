
import os
import re

def task_func(log_file_path: str, keywords: list) -> list:
    formatted_lines = []
    
    # Regular expression pattern to match the timestamp in the log line
    timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"The log file {log_file_path} does not exist.")
    
    with open(log_file_path, 'r') as file:
        for line in file:
            if any(keyword in line for keyword in keywords):
                # Extract the timestamp using regex
                timestamp_match = re.search(timestamp_pattern, line)
                if timestamp_match:
                    timestamp = timestamp_match.group(0)
                    # Remove the timestamp from the line
                    message = line.replace(timestamp, '').strip()
                    # Format the line
                    formatted_line = f"{keyword:<20}{timestamp:<20}{message}"
                    formatted_lines.append(formatted_line)
    
    return formatted_lines