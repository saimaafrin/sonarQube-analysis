
import re
import json
from collections import defaultdict
import string

def task_func(json_string):
    # Parse the JSON string
    data = json.loads(json_string)

    # Extract the text field
    text = data.get("text")

    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Count word frequency
    word_counts = defaultdict(int)
    for word in text.split():
        word_counts[word] += 1

    return word_counts