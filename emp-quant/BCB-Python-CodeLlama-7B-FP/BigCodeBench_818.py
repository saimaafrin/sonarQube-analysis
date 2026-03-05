import re
import string
def task_func(text):
    """
    Divide a string into words, remove punctuation marks and convert them to lowercase letters.
    """
    # Remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Split into words
    words = text.split()
    return words