
import re
import json
from collections import defaultdict
import string

def task_func(json_string):
    # Parse the JSON string and extract the "text" field
    data = json.loads(json_string)
    text = data.get("text")

    # Convert the text to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    # Count the frequency of each word
    word_counts = defaultdict(int)
    for word in text.split():
        word_counts[word] += 1

    return word_counts