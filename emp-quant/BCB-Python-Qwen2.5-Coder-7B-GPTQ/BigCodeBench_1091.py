import ast
import os
import glob
def task_func(directory):
    """
    Converts all Unicode string representations of dictionaries in all text files in the specified directory to Python dictionaries.
    
    Args:
    directory (str): The directory containing text files with dictionary representations.
    
    Returns:
    list: A list of dictionaries extracted from the text files.
    
    Raises:
    ValueError: If there are text file(s) that have invalid dictionary representation.
    """
    dictionaries = []
    # Iterate over all text files in the specified directory
    for file_path in glob.glob(os.path.join(directory, '*.txt')):
        try:
            # Read the content of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Convert the Unicode string representation to a Python dictionary
                dictionary = ast.literal_eval(content)
                dictionaries.append(dictionary)
        except (SyntaxError, ValueError) as e:
            # Raise an error if the dictionary representation is invalid
            raise ValueError(f"Invalid dictionary representation in file: {file_path}") from e
    return dictionaries