
import ast
import re

def task_func(text_file: str) -> list:
    with open(text_file, "r") as f:
        text = f.read()
    # Extract all dictionaries from the text using regular expressions
    regex = r"\{\s*(?P<key>\w+): (?P<value>\w+)\s*\}"
    matches = re.findall(regex, text)
    # Convert the matches to dictionaries
    dictionaries = [ast.literal_eval(match) for match in matches]
    return dictionaries