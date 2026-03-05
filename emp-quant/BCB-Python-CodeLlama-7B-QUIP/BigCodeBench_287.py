
from collections import Counter
import os
import json

def task_func(filename, directory):
    # Create a counter to keep track of the word counts
    word_count = Counter()

    # Loop through all files in the directory
    for file in os.listdir(directory):
        # Open the file and read its contents
        with open(os.path.join(directory, file), 'r') as f:
            contents = f.read()

        # Update the word count with the contents of the file
        word_count.update(contents.split())

    # Write the word count to a JSON file
    with open(filename, 'w') as f:
        json.dump(word_count, f)

    # Return the total number of words
    return sum(word_count.values())