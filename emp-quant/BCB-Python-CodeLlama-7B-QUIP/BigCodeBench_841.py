
import re
import json
from collections import defaultdict
import string

def task_func(json_string):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', '', json_string).lower()

    # Tokenize the text
    words = re.split(r'\W+', text)

    # Create a dictionary to store word counts
    word_counts = defaultdict(int)

    # Loop through each word and increment its count
    for word in words:
        word_counts[word] += 1

    return word_counts