
import pandas as pd
import os
import json
from collections import Counter

def task_func(json_dir_path, word_count):
    # Initialize a counter to store word frequencies
    word_counter = Counter()
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(json_dir_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_dir_path, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                # Extract text content from the JSON data
                if 'text' in data:
                    text = data['text']
                    
                    # Split the text into words and update the counter
                    words = text.split()
                    word_counter.update(words)
    
    # Get the most common words and their counts
    most_common_words = word_counter.most_common(word_count)
    
    return most_common_words