
import os
import re

def task_func(log_file_path: str, keywords: list):
    formatted_lines = []
    keyword_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b')
    
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"The log file {log_file_path} does not exist.")
    
    with open(log_file_path, 'r') as file:
        for line in file:
            if keyword_pattern.search(line):
                timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
                message = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} .+', line)
                if timestamp and message:
                    formatted_line = f"{keyword_pattern.search(line).group():<20}{timestamp.group():<20}{message.group()[len(timestamp.group()):]}"
                    formatted_lines.append(formatted_line)
    
    return formatted_lines