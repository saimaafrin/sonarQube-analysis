
import pandas as pd
import os
import json
from collections import Counter

def task_func(json_dir_path, word_count):
    # Create a list to store the most common words and their counts
    most_common_words = []

    # Iterate over all JSON files in the specified directory
    for file in os.listdir(json_dir_path):
        # Open the JSON file and read its content
        with open(os.path.join(json_dir_path, file), 'r') as f:
            data = json.load(f)

        # Extract the text content from the JSON file
        text = data['text']

        # Tokenize the text content and convert it to lowercase
        tokens = text.lower().split()

        # Create a Counter object to count the frequency of each word
        word_counts = Counter(tokens)

        # Add the most common words and their counts to the list
        most_common_words.extend(word_counts.most_common(word_count))

    # Return the list of most common words and their counts
    return most_common_words