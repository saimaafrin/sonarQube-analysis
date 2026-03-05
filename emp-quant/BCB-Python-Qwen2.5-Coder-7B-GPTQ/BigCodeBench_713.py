import os
import re
def task_func(log_file_path: str, keywords: list):
    formatted_lines = []
    keyword_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b')
    
    with open(log_file_path, 'r') as file:
        for line in file:
            if keyword_pattern.search(line):
                match = keyword_pattern.search(line)
                keyword = match.group(0)
                timestamp = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line).group(0)
                message = re.sub(r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b', '', line).strip()
                formatted_line = f"{keyword:20}{timestamp:20}{message}"
                formatted_lines.append(formatted_line)
    
    return formatted_lines