import pandas as pd
import os
import json
from collections import Counter
def task_func(json_dir_path, word_count):
    """
    Analyze text content in JSON files from a given directory and find the most common words.
    This function reads all the JSON files in the specified directory, extracts the text content from each file, and determines the most frequent words. It then returns a list of the specified number of the most common words and their respective counts.
    """
    # Create a list to store the text content of all JSON files
    text_list = []

    # Iterate over all JSON files in the specified directory
    for file in os.listdir(json_dir_path):
        # Open the JSON file and read its content
        with open(os.path.join(json_dir_path, file), 'r') as f:
            data = json.load(f)

        # Extract the text content from the JSON data
        text = data['text']

        # Add the text content to the list
        text_list.append(text)

    # Join all text content into a single string
    text = ' '.join(text_list)

    # Tokenize the text content into individual words
    words = text.split()

    # Create a Counter object to count the word frequencies
    counter = Counter(words)

    # Get the most common words and their counts
    most_common = counter.most_common(word_count)

    # Return a list of tuples with the most common words and their counts
    return most_common
json_dir_path = 'path/to/json/files'
word_count = 10