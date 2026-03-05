from collections import Counter
import os
import json
def task_func(filename, directory):
    word_counts = Counter()
    total_words = 0

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    # Read the file and count words
                    words = f.read().split()
                    word_counts.update(words)
                    total_words += len(words)

    # Export the counts to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(dict(word_counts), json_file)

    return total_words