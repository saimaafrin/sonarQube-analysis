import pandas as pd
import os
import json
from collections import Counter
def task_func(json_dir_path, word_count):
    """
    Analyze text content in JSON files from a given directory and find the most common words.
    This function reads all the JSON files in the specified directory, extracts the text content from each file, and determines the most frequent words. It then returns a list of the specified number of the most common words and their respective counts.
    Args:
        json_dir_path (str): Path to the directory containing the JSON files.
        word_count (int): Number of most common words to return.
    Returns:
        list: A list of tuples with the most common words and their counts.
    """
    # Create a list to store the text content of all JSON files
    text_list = []

    # Iterate over all JSON files in the directory
    for filename in os.listdir(json_dir_path):
        # Open the JSON file and extract the text content
        with open(os.path.join(json_dir_path, filename), 'r') as f:
            data = json.load(f)
            text = data['text']
            text_list.append(text)

    # Flatten the list of lists into a single list of words
    words = [word for text in text_list for word in text.split()]

    # Create a Counter object to determine the most common words
    counter = Counter(words)

    # Return the top `word_count` most common words and their counts
    return counter.most_common(word_count)