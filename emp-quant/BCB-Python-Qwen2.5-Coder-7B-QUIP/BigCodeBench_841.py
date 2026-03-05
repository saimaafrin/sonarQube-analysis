
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

    # Convert to lowercase and remove punctuation
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text).lower()

    # Split the text into words and count their frequency
    word_counts = defaultdict(int)
    for word in text.split():
        word_counts[word] += 1

    return dict(word_counts)