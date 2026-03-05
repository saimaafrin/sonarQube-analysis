
import re
from collections import Counter

def task_func(input_str):
    # Remove all non-alphanumeric characters
    clean_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)
    # Convert to lowercase
    lower_str = clean_str.lower()
    # Create a dictionary with character frequencies
    char_freq = Counter(lower_str)
    return char_freq