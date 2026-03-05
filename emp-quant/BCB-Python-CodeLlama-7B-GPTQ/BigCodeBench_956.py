import re
import string
import random
def task_func(text: str, seed=None) -> str:
    """
    Transforms a given string by removing special characters, normalizing whitespace, and randomizing character casing.
    """
    # Replace special characters with '_'
    text = re.sub(r'[^a-zA-Z0-9\s]', '_', text)

    # Replace spaces with '__'
    text = re.sub(r'\s+', '__', text)

    # Replace newlines with '___'
    text = re.sub(r'\n+', '___', text)

    # Randomize character casing with a 50% probability
    text = ''.join(random.choice([c.upper(), c.lower()]) for c in text)

    return text