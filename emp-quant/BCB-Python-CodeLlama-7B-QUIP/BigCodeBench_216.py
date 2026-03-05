
import pandas as pd
import os
import json
from collections import Counter

def task_func(json_dir_path, word_count):
    # Read all JSON files in the specified directory
    json_files = [os.path.join(json_dir_path, f) for f in os.listdir(json_dir_path)]
    # Extract the text content from each file
    text_content = [json.loads(f)["text"] for f in json_files]
    # Determine the most frequent words
    counter = Counter(text_content)
    # Return the specified number of the most common words and their counts
    return counter.most_common(word_count)