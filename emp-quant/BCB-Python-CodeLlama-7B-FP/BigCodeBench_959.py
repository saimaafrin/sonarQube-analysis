import string
import random
def task_func(text, seed=None):
    """
    Transforms the input text by replacing each alphabetic character with a random letter, while preserving the case and non-alphabetic characters of the original text.
    """
    if seed is not None:
        random.seed(seed)
    result = ""
    for char in text:
        if char.isalpha():
            result += random.choice(string.ascii_letters)
        else:
            result += char
    return result