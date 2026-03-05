
import re
import string
import random

def task_func(text: str, seed=None) -> str:
    """
    Transforms a given string by removing special characters, normalizing whitespace, and randomizing character casing.
    """
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Randomize character casing
    if seed is not None:
        random.seed(seed)
    for i, c in enumerate(text):
        if random.random() < 0.5:
            text = text[:i] + c.upper() + text[i + 1:]

    return text