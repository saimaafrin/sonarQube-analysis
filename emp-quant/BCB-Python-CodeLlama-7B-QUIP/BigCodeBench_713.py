
import os
import re

def task_func(log_file_path: str, keywords: list):
    formatted_lines = []
    with open(log_file_path, "r") as f:
        for line in f:
            for keyword in keywords:
                if re.search(keyword, line):
                    formatted_line = f"{keyword} {timestamp} {message}"
                    formatted_lines.append(formatted_line)
    return formatted_lines