import ast
import re
def task_func(text_file: str) -> list:
    """
    Extract all string representations of dictionaries from a text file using regular expressions and convert them to Python dictionaries.
    """
    with open(text_file, "r") as f:
        text = f.read()

    pattern = r"\{.*?\}"
    matches = re.findall(pattern, text)

    dictionaries = []
    for match in matches:
        dictionary = ast.literal_eval(match)
        dictionaries.append(dictionary)

    return dictionaries