import re
import string
PUNCTUATION = string.punctuation
def task_func(text):
    """
    Divide a string into words, remove punctuation marks and convert them to lowercase letters.
    """
    # Remove punctuation marks
    text = re.sub(f'[{PUNCTUATION}]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Split into words
    words = text.split()
    return words