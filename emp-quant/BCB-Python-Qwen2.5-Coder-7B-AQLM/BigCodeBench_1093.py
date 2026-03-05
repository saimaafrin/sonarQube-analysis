
import ast
import re

def task_func(text_file: str) -> list:
    dictionaries = []
    with open(text_file, 'r') as file:
        content = file.read()
        # Regular expression to match dictionary-like strings
        dict_pattern = re.compile(r'\{.*?\}')
        matches = dict_pattern.findall(content)
        for match in matches:
            try:
                # Convert string to dictionary using ast.literal_eval for safety
                dictionary = ast.literal_eval(match)
                dictionaries.append(dictionary)
            except (ValueError, SyntaxError):
                # Ignore strings that are not valid dictionaries
                continue
    return dictionaries