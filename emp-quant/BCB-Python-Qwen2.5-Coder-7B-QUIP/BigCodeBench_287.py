
from collections import Counter
import os
import json

def task_func(filename, directory):
    word_count = Counter()
    total_words = 0

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as file:
                for line in file:
                    words = line.split()
                    word_count.update(words)
                    total_words += len(words)

    # Export the word counts to a JSON file
    with open(filename, 'w') as json_file:
        json.dump(word_count, json_file)

    return total_words