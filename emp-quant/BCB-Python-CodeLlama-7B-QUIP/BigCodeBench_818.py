
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Remove punctuation marks
    text = re.sub(PUNCTUATION, '', text)
    # Convert to lowercase
    text = text.lower()
    # Split into words
    words = re.split(r'\W+', text)
    # Remove empty strings
    words = [word for word in words if word != '']
    return words