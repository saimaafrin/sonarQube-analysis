
import re
import json
from collections import defaultdict
import string

def task_func(json_string):
    try:
        data = json.loads(json_string)
        text = data.get('text', '')
    except json.JSONDecodeError:
        return {}

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and non-alphanumeric characters except spaces
    cleaned_text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)

    # Split into words
    words = cleaned_text.split()

    # Count word frequency
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    return dict(word_count)