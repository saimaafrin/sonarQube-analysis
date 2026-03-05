
import ast
import re
def task_func(text_file: str) -> list:
    with open(text_file, 'r') as file:
        content = file.read()
        pattern = r'\{.*\}'
        matches = re.findall(pattern, content)
        dictionaries = [ast.literal_eval(match) for match in matches]
        return dictionaries