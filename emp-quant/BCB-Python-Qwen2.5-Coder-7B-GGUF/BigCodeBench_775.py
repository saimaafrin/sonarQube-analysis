
from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def task_func(string):
    # Use regex to find the prefix before the last '-'
    match = LETTERS_PATTERN.match(string)
    if match:
        prefix = match.group(1)
        # Count the frequency of each lowercase letter in the prefix
        letter_count = Counter(prefix)
        return letter_count
    else:
        return {}