
import ast
import re

def task_func(text_file: str) -> list:
    # Regular expression pattern to match string representations of dictionaries
    dict_pattern = r'\{[^{}]*\}'
    
    # Read the content of the text file
    with open(text_file, 'r') as file:
        content = file.read()
    
    # Find all matches of the dictionary pattern
    dict_strings = re.findall(dict_pattern, content)
    
    # Convert each string representation to a Python dictionary
    dictionaries = [ast.literal_eval(s) for s in dict_strings]
    
    return dictionaries