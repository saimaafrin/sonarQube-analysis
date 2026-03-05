
import re
import string
import random

def task_func(text: str, seed=None) -> str:
    if seed is not None:
        random.seed(seed)

    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Normalize whitespace
    text = re.sub(r'\s+', '_', text)
    text = re.sub(r'\t', '__', text)
    text = re.sub(r'\n', '___', text)

    # Randomize character casing
    result = []
    for char in text:
        if char.isalpha():
            if random.choice([True, False]):
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char)

    return ''.join(result)