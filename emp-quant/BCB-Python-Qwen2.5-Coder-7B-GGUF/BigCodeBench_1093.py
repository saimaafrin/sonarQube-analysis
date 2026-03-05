
import ast
import re

def task_func(text_file: str) -> list:
    with open(text_file, 'r') as file:
        content = file.read()
    
    # Regular expression to find string representations of dictionaries
    dict_pattern = re.compile(r'\{.*?\}')
    
    # Find all matches in the content
    dict_strings = dict_pattern.findall(content)
    
    # Convert string representations of dictionaries to actual Python dictionaries
    dictionaries = [ast.literal_eval(d) for d in dict_strings]
    
    return dictionaries