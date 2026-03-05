import ast
import re
def task_func(text_file: str) -> list:
    """
    Extract all string representations of dictionaries from a text file using regular expressions and convert them to Python dictionaries.
    """
    with open(text_file, "r") as f:
        text = f.read()

    # Find all dictionary string representations in the text
    dict_strs = re.findall(r"\{.*?\}", text)

    # Convert each dictionary string representation to a Python dictionary
    dicts = [ast.literal_eval(dict_str) for dict_str in dict_strs]

    return dicts