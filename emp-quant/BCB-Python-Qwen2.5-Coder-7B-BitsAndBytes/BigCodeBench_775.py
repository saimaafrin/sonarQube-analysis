
from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def task_func(string):
    # Find the prefix before the last '-' using regex
    match = LETTERS_PATTERN.match(string)
    if not match:
        return {}
    
    prefix = match.group(1)
    # Count the frequency of each lowercase letter in the prefix
    letter_count = Counter(prefix.lower())
    
    return dict(letter_count)