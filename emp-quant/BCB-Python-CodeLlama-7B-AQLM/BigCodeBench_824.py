import re
import string
def task_func(text):
    """
    Count the number of words and punctuation marks in a string.

    Parameters:
    - text (str): The input string.

    Returns:
    - tuple: A tuple containing the number of words and punctuation marks.

    Requirements:
    - re
    - string

    Example:
    >>> task_func("Hello, world! This is a test.")
    (6, 3)
    """
    # Split the string into words and punctuation marks
    words = re.split(r'[^\w\s]', text)
    # Count the number of words and punctuation marks
    num_words = len(words) - 1
    num_punctuation = len(words) - num_words
    # Return the number of words and punctuation marks
    return num_words, num_punctuation