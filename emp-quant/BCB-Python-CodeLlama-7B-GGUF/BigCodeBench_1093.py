
import ast
import re

def task_func(text_file: str) -> list:
    """
    Extract all string representations of dictionaries from a text file using regular expressions and convert them to Python dictionaries.

    Args:
        text_file (str): Path to the text file.

    Returns:
        list: A list of dictionaries. Each dictionary is parsed from the text file using regular expressions.
    """
    with open(text_file, 'r') as f:
        text = f.read()

    pattern = r'\{(.*?)\}'
    matches = re.findall(pattern, text)

    dictionaries = []
    for match in matches:
        dictionary = ast.literal_eval(match)
        dictionaries.append(dictionary)

    return dictionaries