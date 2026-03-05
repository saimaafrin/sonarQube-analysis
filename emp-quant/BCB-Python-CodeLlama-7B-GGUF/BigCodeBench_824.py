
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    """
    Count the number of words and punctuation marks in a string.

    Args:
        text (str): The input string.

    Returns:
        tuple: A tuple containing the number of words and punctuation marks.
    """
    words = re.split(r'\W+', text)
    punctuation = len(re.findall(r'\W+', text))
    return (len(words), punctuation)