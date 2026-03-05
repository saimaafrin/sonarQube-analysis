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

        # Extract the text content from the JSON file
        text = data['text']

        # Add the text content to the list
        text_list.append(text)

    # Flatten the list of text content into a single string
    text_string = ' '.join(text_list)

    # Tokenize the text string into individual words
    words = text_string.split()

    # Create a Counter object to count the frequency of each word
    word_counts = Counter(words)

    # Sort the Counter object by word frequency
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top N most common words and their counts
    return sorted_word_counts[:word_count]
json_dir_path = 'path/to/json/files'
word_count = 5