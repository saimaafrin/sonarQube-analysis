import re
import string
PUNCTUATION = string.punctuation
def task_func(text):
    # Split the text into words
    words = re.findall(r'\b\w+\b', text)
    # Count the number of words
    num_words = len(words)
    # Count the number of punctuation marks
    num_punctuation = sum(1 for char in text if char in PUNCTUATION)
    # Return the results as a tuple
    return (num_words, num_punctuation)