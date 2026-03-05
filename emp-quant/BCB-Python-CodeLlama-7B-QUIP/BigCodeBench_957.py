
import string
import re

def task_func(text: str) -> tuple:
    # Remove all special characters and whitespace
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Split the text into individual words
    words = text.split()

    # Count the number of words
    num_words = len(words)

    # Count the number of unique characters
    unique_chars = set(text)
    num_unique_chars = len(unique_chars)

    return num_words, num_chars, num_unique_chars