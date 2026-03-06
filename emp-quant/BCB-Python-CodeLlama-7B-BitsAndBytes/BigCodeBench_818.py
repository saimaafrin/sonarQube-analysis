
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Remove punctuation marks and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

    # Split the text into words
    cleaned_words = cleaned_text.split()

    return cleaned_words