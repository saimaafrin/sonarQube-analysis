
from collections import Counter
import os
import json

def task_func(filename, directory):
    # Initialize a counter for the total number of words
    total_words = Counter()

    # Iterate over the files in the directory
    for file in os.listdir(directory):
        # Check if the file is a .txt file
        if file.endswith('.txt'):
            # Open the file and read its contents
            with open(os.path.join(directory, file), 'r') as f:
                contents = f.read()

            # Split the contents into individual words
            words = contents.split()

            # Add the number of words in the file to the total counter
            total_words.update(words)

    # Export the total number of words to a JSON file
    with open(filename, 'w') as f:
        json.dump(total_words, f)

    # Return the total number of words
    return len(total_words)