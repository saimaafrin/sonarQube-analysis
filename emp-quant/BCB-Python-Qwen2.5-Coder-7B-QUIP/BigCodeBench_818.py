
import re
import string
# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Split the text into words
    words = text.split()
    
    # Remove punctuation and convert to lowercase
    cleaned_words = [''.join(filter(lambda x: x not in PUNCTUATION, word)).lower() for word in words]
    
    return cleaned_words