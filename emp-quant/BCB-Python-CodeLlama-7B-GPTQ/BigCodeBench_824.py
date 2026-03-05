import re
import string
PUNCTUATION = string.punctuation
def task_func(text):
    """
    Count the number of words and punctuation marks in a string.

    Args:
        text (str): The input string.

    Returns:
        tuple: A tuple containing the number of words and punctuation marks.
    """
    # Split the string into words and punctuation marks
    words = re.split(r'\W+', text)
    punctuation = [char for char in text if char in PUNCTUATION]

    # Count the number of words and punctuation marks
    num_words = len(words)
    num_punctuation = len(punctuation)

    # Return the result as a tuple
    return num_words, num_punctuation
text = "Hello, World! How are you?"