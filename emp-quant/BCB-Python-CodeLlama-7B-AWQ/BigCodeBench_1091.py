import ast
import os
import glob
def task_func(directory):
    """
    Convert all Unicode string representations of dictionaries in all text files in the specified directory to Python dictionaries.
    """
    # Ensure that the text files in the directory contain valid Unicode string representations of dictionaries
    if not os.path.isdir(directory):
        raise ValueError(f"{directory} is not a valid directory")
    if not os.listdir(directory):
        raise ValueError(f"{directory} is empty")
    if not all(os.path.isfile(os.path.join(directory, file)) for file in os.listdir(directory)):
        raise ValueError(f"{directory} contains non-file entries")
    if not all(file.endswith(".txt") for file in os.listdir(directory)):
        raise ValueError(f"{directory} contains non-text files")
    # Extract dictionaries from text files
    dictionaries = []
    for file in os.listdir(directory):
        with open(os.path.join(directory, file), "r") as f:
            try:
                dictionaries.append(ast.literal_eval(f.read()))
            except ValueError:
                raise ValueError(f"{file} contains invalid dictionary representation")
    return dictionaries