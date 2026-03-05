import string
import re
def task_func(text: str) -> tuple:
    """
    Counts the number of words, characters, and unique characters in a given text.
    Note that: This function considers whitespace-separated substrings as words.
    When counting characters, this function excludes whitespace and special characters (i.e. string.punctuation).
    The function should output with:
        tuple: A tuple containing three integers: the number of words,
        the number of characters,
        the number of unique characters.
    """
    # Remove all whitespace and special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Count the number of words
    words = len(text.split())

    # Count the number of characters
    characters = len(text)

    # Count the number of unique characters
    unique_chars = len(set(text))

    return words, characters, unique_chars