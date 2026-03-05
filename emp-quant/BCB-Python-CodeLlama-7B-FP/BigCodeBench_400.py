import json
from glob import glob
def task_func(directory, string):
    """
    Search for a specific string within the JSON data of files in a given directory and its subdirectories.
    This function recursively scans the specified directory for JSON files, then checks each file to see if the given string is present within the JSON data structure.
    Note that:
    - The string search is case-sensitive and looks for a match within the structure of the JSON data, not just as a substring in the file content.
    - If the directory does not contain any JSON files or if no JSON files contain the string, an empty list is returned.
    """
    file_paths = []
    for file_path in glob(f"{directory}/**/*.json", recursive=True):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if string in data:
                    file_paths.append(file_path)
            except json.JSONDecodeError:
                pass
    return file_paths