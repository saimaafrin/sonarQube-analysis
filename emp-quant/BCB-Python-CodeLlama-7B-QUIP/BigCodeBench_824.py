
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Remove all punctuation
    text = re.sub(r'[{punctuation}]', '', text)
    # Split the text into words
    words = text.split()
    # Count the number of words
    num_words = len(words)
    # Count the number of punctuation marks
    num_punctuation = len(text) - num_words
    return num_words, num_punctuation