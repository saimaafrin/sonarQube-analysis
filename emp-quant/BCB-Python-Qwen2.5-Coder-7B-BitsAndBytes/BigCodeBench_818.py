
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Remove punctuation using regex
    text = re.sub(f'[{re.escape(PUNCTUATION)}]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Split the text into words
    cleaned_words = text.split()
    return cleaned_words