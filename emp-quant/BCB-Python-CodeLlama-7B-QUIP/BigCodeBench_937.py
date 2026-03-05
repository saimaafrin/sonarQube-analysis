
import re
from collections import Counter

def task_func(input_str):
    # Remove all non-alphanumeric characters
    cleaned_str = re.sub("[^a-zA-Z0-9]", "", input_str)
    # Convert to lowercase
    lowercase_str = cleaned_str.lower()
    # Count the frequency of each character
    char_freq = Counter(lowercase_str)
    # Return the dictionary of character frequencies
    return char_freq