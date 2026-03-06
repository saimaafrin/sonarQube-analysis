
import re
import os
import shutil
from datetime import datetime

def task_func(directory):
    # Dictionary to store files organized by their category
    organized_files = {}
    
    # Regular expression to find the first text not enclosed in square brackets
    pattern = r'(?<!\[)[^\[\]]+(?!\])'
    
    # Walk through all files in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    match = re.search(pattern, content)
                    if match:
                        category = match.group(0).strip()
                        if category not in organized_files:
                            organized_files[category] = []
                        organized_files[category].append(file_path)
                    else:
                        print(f"No matching text found in {file_path}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
    
    # Create subdirectories and move files accordingly
    for category, files in organized_files.items():
        category_dir = os.path.join(directory, category)
        os.makedirs(category_dir, exist_ok=True)
        for file_path in files:
            shutil.move(file_path, category_dir)
    
    return (directory, organized_files)