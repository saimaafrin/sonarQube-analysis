import ast
import re
def task_func(text_file: str) -> list:
    """
    Extract all string representations of dictionaries from a text file using regular expressions and convert them to Python dictionaries.
    """
    with open(text_file, "r") as f:
        text = f.read()

    # Find all dictionary string representations in the text
    pattern = re.compile(r"\{.*?\}")
    matches = pattern.findall(text)

    # Convert each match to a Python dictionary
    dictionaries = [ast.literal_eval(match) for match in matches]

    return dictionaries