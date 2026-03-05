
from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def task_func(string):
    # Extract the prefix before the last hyphen
    match = LETTERS_PATTERN.match(string)
    if match:
        prefix = match.group(1)
    else:
        raise ValueError("Input string does not match the expected format")
    
    # Count the frequency of each lowercase letter in the prefix
    letter_counts = Counter(filter(str.islower, prefix))
    
    return dict(letter_counts)