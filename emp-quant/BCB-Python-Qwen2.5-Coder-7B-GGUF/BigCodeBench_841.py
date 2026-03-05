
import re
import json
from collections import defaultdict
import string

def task_func(json_string):
    try:
        data = json.loads(json_string)
        text = data.get('text', '')
    except (json.JSONDecodeError, KeyError):
        return {}

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and non-alphanumeric characters (except spaces)
    text = re.sub(f'[{string.punctuation}]', '', text)

    # Split the text into words
    words = text.split()

    # Count word frequency
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    return dict(word_count)