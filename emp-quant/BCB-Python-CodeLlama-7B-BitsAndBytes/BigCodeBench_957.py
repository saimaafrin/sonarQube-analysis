
import string
import re

def task_func(text: str) -> tuple:
    """
    Counts the number of words, characters, and unique characters in a given text.

    Args:
        text (str): The text to be counted.

    Returns:
        tuple: A tuple containing three integers: the number of words,
        the number of characters,
        the number of unique characters.
    """
    # Remove all whitespace and special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into words
    words = text.split()

    # Count the number of words
    num_words = len(words)

    # Count the number of characters
    num_chars = len(text)

    # Count the number of unique characters
    unique_chars = len(set(text))

    return num_words, num_chars, unique_chars