
from collections import Counter
import os
import json

def task_func(filename, directory):
    # Create a Counter object to count the number of words in each .txt file
    counter = Counter()

    # Iterate over the files in the specified directory
    for file in os.listdir(directory):
        # Check if the file is a .txt file
        if file.endswith('.txt'):
            # Open the file and read its contents
            with open(os.path.join(directory, file), 'r') as f:
                # Split the contents of the file into words
                words = f.read().split()
                # Update the Counter object with the number of words in the file
                counter.update(words)

    # Export the counts to a JSON file
    with open('word_counts.json', 'w') as f:
        json.dump(counter.most_common(), f)

    # Return the total number of words
    return sum(counter.values())

# Call the function with the specified filename and directory
total_words = task_func('word_counts.json', 'path/to/directory')

# Print the total number of words
print(total_words)