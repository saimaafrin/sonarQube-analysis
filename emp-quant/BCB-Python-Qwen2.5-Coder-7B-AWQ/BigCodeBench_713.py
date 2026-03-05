import os
import re
def task_func(log_file_path: str, keywords: list):
    formatted_lines = []
    keyword_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b')
    
    with open(log_file_path, 'r') as file:
        for line in file:
            if keyword_pattern.search(line):
                parts = line.split()
                timestamp = parts[0] + ' ' + parts[1]
                message = ' '.join(parts[4:])
                formatted_line = f"{parts[3]:<20}{timestamp:<20}{message}"
                formatted_lines.append(formatted_line)
    
    return formatted_lines