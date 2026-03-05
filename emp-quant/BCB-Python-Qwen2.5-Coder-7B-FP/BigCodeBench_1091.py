import ast
import os
import glob
def task_func(directory):
    """
    Converts all Unicode string representations of dictionaries in all text files in the specified directory to Python dictionaries.
    
    Args:
    directory (str): The directory containing the text files.
    
    Returns:
    list: A list of dictionaries extracted from the text files.
    
    Raises:
    ValueError: If there are text file(s) that have invalid dictionary representation.
    """
    # Initialize an empty list to store the dictionaries
    dictionaries = []
    
    # Use glob to find all text files in the specified directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))
    
    for file_path in text_files:
        try:
            # Open the file and read its content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Use ast.literal_eval to safely evaluate the string as a Python literal
                dictionary = ast.literal_eval(content)
                
                # Check if the evaluated content is a dictionary
                if isinstance(dictionary, dict):
                    dictionaries.append(dictionary)
                else:
                    raise ValueError(f"Invalid dictionary representation in file: {file_path}")
        except (SyntaxError, ValueError) as e:
            # Raise a ValueError if there is an invalid dictionary representation
            raise ValueError(f"Invalid dictionary representation in file: {file_path}") from e
    
    return dictionaries