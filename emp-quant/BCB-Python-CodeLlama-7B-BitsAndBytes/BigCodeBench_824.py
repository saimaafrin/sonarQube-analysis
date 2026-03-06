
import re
import string

# Constants
PUNCTUATION = string.punctuation

def task_func(text):
    # Split the text into individual characters
    chars = list(text)

    # Initialize variables to count words and punctuation marks
    num_words = 0
    num_punct = 0

    # Iterate over the characters and count words and punctuation marks
    for char in chars:
        if char in PUNCTUATION:
            num_punct += 1
        elif char.isalpha():
            num_words += 1

    # Return a tuple containing the number of words and punctuation marks
    return num_words, num_punct