
from collections import Counter
import os
import json

def task_func(filename, directory):
    word_counts = Counter()
    
    # Walk through all directories and files in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    words = content.split()
                    word_counts.update(words)
    
    # Export the word counts to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(word_counts, json_file, indent=4)
    
    # Return the total number of words
    total_words = sum(word_counts.values())
    return total_words