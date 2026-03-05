import pandas as pd
import os
import json
from collections import Counter
def task_func(json_dir_path, word_count):
    # Initialize a list to hold all words from all JSON files
    all_words = []
    
    # Loop through each file in the directory
    for filename in os.listdir(json_dir_path):
        if filename.endswith('.json'):
            # Construct the full file path
            file_path = os.path.join(json_dir_path, filename)
            # Open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Extract text content and split into words
                text = data.get('text', '')
                words = text.split()
                # Add words to the list
                all_words.extend(words)
    
    # Count the frequency of each word
    word_counts = Counter(all_words)
    
    # Get the most common words
    most_common_words = word_counts.most_common(word_count)
    
    return most_common_words