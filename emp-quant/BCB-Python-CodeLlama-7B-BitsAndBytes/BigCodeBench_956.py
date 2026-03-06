
import re
import string
import random

def task_func(text: str, seed=None) -> str:
    """
    Transforms a given string by removing special characters, normalizing whitespace, and randomizing character casing.

    Args:
        text (str): The input text string.
        seed (int, optional): A random seed for reproducibility. Defaults to None.

    Returns:
        str: The preprocessed text string.
    """
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    # Randomize character casing
    if seed is not None:
        random.seed(seed)
    for i in range(len(text)):
        if random.random() < 0.5:
            text = text[:i] + text[i].upper() + text[i+1:]

    return text