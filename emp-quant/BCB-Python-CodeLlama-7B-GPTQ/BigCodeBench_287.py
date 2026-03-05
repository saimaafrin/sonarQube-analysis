from collections import Counter
import os
import json
def task_func(filename, directory):
    """
    Count the number of words in .txt files within a specified directory, export the counts to a JSON file, and then return the total number of words.
    """
    # Create a Counter object to count the number of words in each file
    counter = Counter()

    # Iterate over all files in the directory
    for file in os.listdir(directory):
        # Check if the file is a .txt file
        if file.endswith('.txt'):
            # Open the file and read its contents
            with open(os.path.join(directory, file), 'r') as f:
                contents = f.read()

            # Split the contents into individual words
            words = contents.split()

            # Add the number of words in the file to the Counter
            counter.update(words)

    # Export the Counter to a JSON file
    with open(filename, 'w') as f:
        json.dump(counter, f)

    # Return the total number of words
    return counter.total()
filename = 'words.json'
directory = '.'