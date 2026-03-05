import re
import string
def task_func(text):
    """
    Count the number of words and punctuation marks in a string.

    Args:
        text (str): The input string.

    Returns:
        tuple: A tuple containing the number of words and punctuation marks.
    """
    # Remove all punctuation marks from the input string
    text = re.sub(r'[^\w\s]', '', text)

    # Split the string into words
    words = text.split()

    # Count the number of words
    num_words = len(words)

    # Count the number of punctuation marks
    num_punctuation = len(text) - num_words

    return num_words, num_punctuation