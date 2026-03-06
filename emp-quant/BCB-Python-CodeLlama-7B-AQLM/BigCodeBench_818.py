import re
import string
def task_func(text):
    """
    Divide a string into words, remove punctuation marks and convert them to lowercase letters.

    Parameters:
    - text (str): The input string.

    Returns:
    - cleaned_words (list): A list of cleaned words.

    Requirements:
    - re
    - string

    Example:
    >>> task_func("Hello, world! This is a test.")
    ['hello', 'world', 'this', 'is', 'a', 'test']
    """
    # Split the string into words
    words = re.split(r'[^\w\s]', text)

    # Remove punctuation marks
    cleaned_words = []
    for word in words:
        cleaned_word = re.sub(r'[^\w]', '', word)
        cleaned_words.append(cleaned_word.lower())

    return cleaned_words