
import pandas as pd
import os
import json
from collections import Counter

def task_func(json_dir_path, word_count):
    # Initialize a Counter to store word counts
    word_counter = Counter()

    # List all files in the directory
    files = os.listdir(json_dir_path)

    # Iterate over each file
    for file in files:
        # Check if the file is a JSON file
        if file.endswith('.json'):
            # Open and read the JSON file
            with open(os.path.join(json_dir_path, file), 'r') as f:
                data = json.load(f)
                # Assuming the text content is stored in a key called 'text'
                if 'text' in data:
                    # Split the text into words and update the counter
                    words = data['text'].split()
                    word_counter.update(words)

    # Get the most common words and their counts
    most_common_words = word_counter.most_common(word_count)

    # Return the list of tuples with the most common words and their counts
    return most_common_words