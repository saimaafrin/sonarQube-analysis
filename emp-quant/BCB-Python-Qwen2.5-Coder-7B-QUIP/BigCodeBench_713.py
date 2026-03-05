
import os
import re

def task_func(log_file_path: str, keywords: list):
    formatted_lines = []
    with open(log_file_path, 'r') as file:
        for line in file:
            for keyword in keywords:
                if re.search(keyword, line):
                    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line)
                    if match:
                        timestamp = match.group(1)
                        message = re.sub(r'\s+', ' ', ' '.join(line.split()[len(timestamp):]))
                        formatted_line = f"{keyword}: {timestamp}{' ' * 20}{message.strip()}"
                        formatted_lines.append(formatted_line)
    return formatted_lines